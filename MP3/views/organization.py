from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB

import pycountry
organization = Blueprint('organization', __name__, url_prefix='/organization')

@organization.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve id, name, address, city, country, state, zip, website, donation count as donations for the organization
    # don't do SELECT * and replace the below "..." portion
    allowed_columns = ["name", "city", "country", "state", "modified", "created"]
    query = """SELECT
            organization.id,
            organization.name,
            organization.address,
            organization.city,
            organization.country,
            organization.state,
            organization.zip,
            organization.website,
            COUNT(donation.id) AS donations
        FROM
            IS601_MP3_Organizations organization
        LEFT JOIN
            IS601_MP3_Donations donation ON organization.id = donation.organization_id
        WHERE 1=1
        """
    args = {} # <--- add values to replace %s/%(named)s placeholders
    
    # TODO search-2 get name, country, state, column, order, limit request args
    name = request.args.get('name')
    country = request.args.get('country')
    state = request.args.get('state')
    column = request.args.get('column')
    order = request.args.get('order')
    limit = request.args.get('limit')

    args['order'] = request.args.get('order')
    args['limit'] = request.args.get('limit')

    # TODO search-3 append a LIKE filter for name if provided
    if name:
        query += " AND organization.name LIKE %(name)s" 
        args['name'] = f"%{name}%"
    # TODO search-4 append an equality filter for country if provided
    if country:
        query += " AND organization.country = %(country)s"
        args['country'] = f"%{country}%"
    # TODO search-5 append an equality filter for state if provided
    if state:
        query += " AND organization.state = %(state)s"
        args['state'] = f"%{state}%"
    query+= """
            GROUP BY
            organization.id
            """
    # TODO search-6 append sorting if column and order are provided and within the allows columns and allowed order asc,desc
    if column and order and column in allowed_columns and order in ("asc", "desc"):
        column = "organization." + str(column)
        query += f"ORDER BY {column} {order}"
        args['column'] = f"%{column}%"

   
    # TODO search-7 append limit (default 10) or limit greater than or equal to 1 and less than or equal to 100
    # TODO search-8 provide a proper error message if limit isn't a number or if it's out of bounds
    limit = 10 # TODO change this per the above requirements
    if not limit:
        limit = 10
    query += " LIMIT "+str(limit)
    args["limit"] = limit
    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, args)
        #print(f"result {result.rows}")
        if result.status:
            rows = result.rows
    except Exception as e:
        # TODO search-9 make message user friendly
        flash(str(e), "danger")
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    
    # do this prior to passing to render_template, but not before otherwise it can break validation
    
    return render_template("list_organizations.html", rows=rows, allowed_columns=allowed_columns)


@organization.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        has_error = False # use this to control whether or not an insert occurs

        
        # TODO add-1 retrieve form data for name, address, city, state, country, zip, website, description
        name = request.form.get('name')
        address = request.form.get('address')
        city = request.form.get('city')
        state = request.form.get('state')
        country = request.form.get('country')
        zipcode = request.form.get('zip')
        website = request.form.get('website')
        description = request.form.get('description')
        # TODO add-2 name is required (flash proper error message)
        if not name:
                flash('Name is required','danger')
                has_error = True
        # TODO add-3 address is required (flash proper error message)
        if not address:
                flash('Address is required','danger')
                has_error = True
        
        # TODO add-4 city is required (flash proper error message)
        if not city:
                flash('City is required','danger')
                has_error = True
        # TODO add-5 state is required (flash proper error message)
        if not state:
                flash('State is required','danger')
                has_error = True
        # TODO add-5a state should be a valid state mentioned in pycountry for the selected state
        # Get a list of valid state codes for the selected country
        try:
            states = list(pycountry.subdivisions.get(country_code=country))
            state_codes = [s.code for s in states]
        except:
            has_error = True
        # Check if the provided state code is in the list of valid state codes
        if str(country + "-" +state) not in state_codes:
            flash('Not a valid State', 'danger')
            has_error = True
        # hint see geography.py and pycountry documentation to solve this
        # TODO add-6 country is required (flash proper error message)
        if not country:
                flash('Country is required','danger')
                has_error = True
        # TODO add-6a country should be a valid country mentioned in pycountry
        #print(state,country)
        countries = map(lambda c: {"code": c.alpha_2, "name": c.name},list(pycountry.countries))
        country_codes = [c['code'] for c in countries]
        #print(country not in country_codes)
        #print(country_codes)
        if country not in country_codes:
            flash('Not a valid Country','danger')
            has_error = True
        # hint see geography.py and pycountry documentation to solve this
        # TODO add-7 website is not required
        # TODO add-8 zip is required (flash proper error message)
        if not zipcode:
                flash('Zipcode is required','danger')
                has_error = True
        # note: call zip variable zipcode as zip is a built in function it could lead to issues
        # TODO add-9 description is not required

        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO IS601_MP3_Organizations (name, address, city, state, country, zip, website, description)
                VALUES
                (%(name)s, %(address)s, %(city)s, %(state)s, %(country)s, %(zip)s, %(website)s, %(description)s)
                """, {
                    'name':name,
                    'address':address,
                    'city':city,
                    'state':state,
                    'country':country,
                    'zip':zipcode,
                    'website':website,
                    'description':description,
                }) # <-- TODO add-10 add query and add arguments
                
                if result.status:
                    flash("Added Organization", "success")
            except Exception as e:
                # TODO add-11 make message user friendly
                flash(str(e), "danger")
        
    return render_template("manage_organization.html", org=request.form)

@organization.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    row = {}
    id = False
    id = request.args.get('id')
    print(id)

    if not id: # TODO update this for TODO edit-1
        pass
    else:
        if request.method == "POST":
            data = {"id": id} # use this as needed, can convert to tuple if necessary
            # TODO edit-2 retrieve form data for name, address, city, state, country, zip, website
            name = request.form.get('name')
            address = request.form.get('address')
            city = request.form.get('city')
            state = request.form.get('state')
            country = request.form.get('country')
            zipcode = request.form.get('zip')
            website = request.form.get('website')
            description = request.form.get('description')
            data['name'] = name
            data['address'] = address
            data['city'] = city
            data['state'] = state
            data['country'] = country
            data['website'] = website
            data['zip'] = zipcode
            data['description'] = description

            has_error = False # use this to control whether or not an insert occurs
            # TODO edit-3 name is required (flash proper error message)
            if not name:
                flash("Name is required",'danger')
                has_error = True
            # TODO edit-4 address is required (flash proper error message)
            if not address:
                flash("Address is required",'danger')
                has_error = True
            # TODO edit-5 city is required (flash proper error message)
            if not city:
                flash("City is required",'danger')
                has_error = True
            # TODO edit-6 state is required (flash proper error message)
            if not state:
                flash("State is required",'danger')
                has_error = True
            # TODO edit-6a state should be a valid state mentioned in pycountry for the selected state
            # hint see geography.py and pycountry documentation
            try:
                states = list(pycountry.subdivisions.get(country_code=country))
                state_codes = [s.code for s in states]
            except:
                has_error = True
            # Check if the provided state code is in the list of valid state codes
            #print(str(country + "-" +state))
            #print( str(country + "-" +state) not in state_codes)
            if str(country + "-" +state) not in state_codes:
                flash('Not a valid State', 'danger')
                has_error = True
            # TODO edit-7 country is required (flash proper error message)
            if not country:
                flash("Country is required",'danger')
                has_error = True
            # TODO edit-7a country should be a valid country mentioned in pycountry
            # hint see geography.py and pycountry documentation
            countries = map(lambda c: {"code": c.alpha_2, "name": c.name},list(pycountry.countries))
            country_codes = [c['code'] for c in countries]
            #print(country not in country_codes)
            #print(country_codes)
            if country not in country_codes:
                flash('Not a valid Country','danger')
                has_error = True
            # TODO edit-8 website is not required
            # TODO edit-9 zipcode is required (flash proper error message)
            if not zipcode:
                flash("Zipcode is required",'danger')
                has_error = True
            # note: call zip variable zipcode as zip is a built in function it could lead to issues
            # populate data dict with mappings

            if not has_error:
                try:
                    # TODO edit-10 fill in proper update query
                    result = DB.update(""" 
                    UPDATE IS601_MP3_Organizations
                    SET
                    name = %(name)s,
                    address = %(address)s,
                    city = %(city)s,
                    state = %(state)s,
                    country = %(country)s,
                    zip = %(zip)s,
                    website = %(website)s,
                    description = %(description)s
                    WHERE id = %(id)s         
                    """, data)
                    
                    if result.status:
                        print("updated record")
                        flash("Updated record", "success")
                except Exception as e:
                    # TODO edit-11 make this user-friendly
                    print(f"{e}")
                    flash(str(e), "danger")
        try:
            # TODO edit-12 fetch the updated data
            result = DB.selectOne("""SELECT
                id,
                name,
                address,
                city,
                state,
                country,
                zip,
                website,
                description
            FROM IS601_MP3_Organizations 
            WHERE id = %s
            """, id)
            if result.status:
                row = result.row
                
        except Exception as e:
            # TODO edit-13 make this user-friendly
            flash(str(e), "danger")
    
    return render_template("manage_organization.html", org=row)

@organization.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 if id is missing, flash necessary message and redirect to search
    # TODO delete-2 delete organization by id (note: you'll likely need to trigger a delete of all donations related to this organization first due to foreign key constraints)
    # TODO delete-3 ensure a flash message shows for successful delete
    # TODO delete-4 pass all argument except id to this route
    # TODO delete-5 redirect to organization search
    id = request.args.get('id')
    args = {**request.args}
    if not id:
        flash('Select correct ID','danger')
    if id:
        try:
            result = DB.delete("DELETE FROM IS601_MP3_Donations WHERE organization_id = %s", id)
            if result.status:
                flash("Deleted All Donations related to Organization", "success")
            result1 = DB.delete("DELETE FROM IS601_MP3_Organizations WHERE id = %s", id)
            if result1.status:
                flash("Deleted Organization", "success")
        except Exception as e:
            print(e)
            flash(e, "danger")
        del args["id"]
    return redirect(url_for("organization.search", **args))