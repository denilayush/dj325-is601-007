import csv
import io
from flask import Blueprint, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
from sql.db import DB
import traceback
admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route("/import", methods=["GET","POST"])
def importCSV():
    if request.method == "POST":
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file', "warning")
            return redirect(request.url)
        # TODO importcsv-1 check that it's a .csv file, return a proper flash message if it's not and don't attempt to process the file
        if ".csv" not in file.filename:
            flash('Select CSV file',"warning")
            return redirect(request.url)
        if file and secure_filename(file.filename):
            organizations = []
            donations = []
            # DON'T EDIT
            organization_query = """
            INSERT INTO IS601_MP3_Organizations (name, address, city, country, state, zip, website, description)
                        VALUES (%(name)s, %(address)s, %(city)s, %(country)s, %(state)s, %(zip)s, %(website)s, %(description)s)
                        ON DUPLICATE KEY UPDATE 
                        address=values(address),
                        city=values(city),
                        country=values(country),
                        state=values(state),
                        zip=values(zip),
                        website=values(website), 
                        description=values(description)
            """
            # DON'T EDIT
            donation_query = """
            INSERT INTO IS601_MP3_Donations (donor_firstname, donor_lastname, donor_email, item_name, item_description, item_quantity, organization_id, donation_date, comments)
                    VALUES (%(donor_firstname)s, %(donor_lastname)s, %(donor_email)s, %(item_name)s, %(item_description)s, %(quantity)s, 
                            (SELECT id FROM IS601_MP3_Organizations WHERE name = %(organization_name)s LIMIT 1), 
                            %(donation_date)s, %(comments)s)
                    ON DUPLICATE KEY UPDATE 
                                            donor_firstname=%(donor_firstname)s,
                                            donor_lastname=%(donor_lastname)s,
                                            donor_email=%(donor_email)s,
                                            item_name=%(item_name)s, 
                                            item_quantity = %(quantity)s,
                                            item_description= %(item_description)s,
                                            comments=%(comments)s, 
                                            organization_id = (SELECT id FROM IS601_MP3_Organizations WHERE name=%(organization_name)s LIMIT 1),
                                            donation_date = %(donation_date)s,
                                            comments=%(comments)s
            """
            # Note: this reads the file as a stream instead of requiring us to save it, don't modify/remove it
            stream = io.TextIOWrapper(file.stream._file, "UTF8", newline=None)
            # TODO importcsv-2 read the csv file stream as a dict
            organization_names =[]
            for row in csv.DictReader(stream):
                #pass 
                # print(row) #example
                # TODO importcsv-3: extract organization data and append to organization list
                # as a dict only with organization data if all organization fields are present (refer to above SQL)
                #(name, address, city, country, state, zip, website, description)
                # original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
                # keys_to_select = ['a', 'c']
                # subset_dict = {key: original_dict[key] for key in keys_to_select}
                keysOfOrganizations = set(['organization_name', 'organization_address', 'organization_city', 'organization_country', 'organization_state', 'organization_zip', 'organization_website', 'organization_description'])
                if keysOfOrganizations.issubset(row.keys()) and row['organization_name'] not in organization_names:
                    organization_names.append(row['organization_name'])
                    organization = {}
                    organization['name'] = row['organization_name']
                    organization['address'] = row['organization_address']
                    organization['city'] = row['organization_city']
                    organization['country'] = row['organization_country']
                    organization['state'] = row['organization_state']
                    organization['zip'] = row['organization_zip']
                    organization['website'] = row['organization_website']
                    organization['description'] = row['organization_description']
                    organizations.append(organization)
                # TODO importcsv-4: extract donation data and append to donation list
                # as a dict only with donation data if all donation fields are present (refer to above SQL)
                #(donor_firstname, donor_lastname, donor_email, item_name, item_description, item_quantity, organization_id, donation_date, comments)
                full_name = row["donor_name"]
                split_names = full_name.split()  # Split by whitespace
                if len(split_names)== 2:
                    row['first_name'],row['last_name'] = split_names[0],split_names[1]
                elif len(split_names)>2:
                    row['first_name'],row['last_name'] = split_names[1],split_names[2]
                else:
                    continue
                keysOfDonation = set(['first_name', 'last_name', 'donor_email', 'item_name', 'item_description', 'item_quantity', 'organization_name', 'donation_date', 'comments'])
                # print(row,keysOfDonation.issubset(row.keys()))
                if keysOfDonation.issubset(row.keys()):
                    donation = {}
                    donation['donor_firstname'] = row['first_name']
                    donation['donor_lastname'] = row['last_name']
                    donation['donor_email'] = row['donor_email']
                    donation['item_name'] = row['item_name']
                    donation['item_description'] = row['item_description']
                    donation['quantity'] = row['item_quantity']
                    donation['organization_name'] = row['organization_name']
                    donation['donation_date'] = row['donation_date']
                    donation['comments'] = row['comments']

                    donations.append(donation)
                
                
            if len(organizations) > 0:
                print(f"Inserting or updating {len(organizations)} organizations")
                try:
                    result = DB.insertMany(organization_query, organizations)
                    # TODO importcsv-5 display flash message about number of organizations inserted
                    Message = len(organizations),"Organizations Inserted"
                    flash(Message,"success")
                except Exception as e:
                    traceback.print_exc()
                    flash("There was an error loading in the csv data", "danger")
            else:
                # TODO importcsv-6 display flash message (info) that no organizations were loaded
                flash('No organizations were loaded',"info")
                pass
            if len(donations) > 0:
                print(f"Inserting or updating {len(donations)} donations")
                try:
                    result = DB.insertMany(donation_query, donations)
                    # TODO importcsv-7 display flash message about number of donations loaded
                    Message = len(donations),"donations Inserted"
                    flash(Message,"success")
                except Exception as e:
                    traceback.print_exc()
                    flash("There was an error loading in the csv data", "danger")
            else:
                # TODO importcsv-8 display flash message (info) that no donations were loaded
                flash('No donations were loaded',"info")
                pass
            try:
                result = DB.selectOne("SHOW SESSION STATUS LIKE 'questions'")
                print(f"Result {result}")
            except Exception as e:
                    traceback.print_exc()
                    flash("There was an error counting session queries", "danger")
    return render_template("upload.html")