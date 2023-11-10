import datetime
from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
donations = Blueprint('donations', __name__, url_prefix='/donations')


@donations.route("/search", methods=["GET"])
def search():
    rows = []
    organization_name = ""
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve donation id as id, donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description, item_quantity, donation_date, comments, organization_name using a LEFT JOIN
    query = """ 
    SELECT 
    donation.id,donor_firstname,donor_lastname,donor_email,organization_id,item_name,item_description,item_quantity,donation_date,comments,organization.name
    FROM IS601_MP3_Donations donation LEFT JOIN IS601_MP3_Organizations organization ON donation.organization_id = organization.id WHERE 1=1"""
    args = {} # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["donor_firstname", "donor_lastname", "donor_email", "organization_name" ,"item_name", "item_quantity", "created", "modified"]
    # TODO search-2 get fn, ln, email, organization_id, column, order, limit from request args
    fn = request.args.get("fn")
    ln = request.args.get("ln")
    email = request.args.get("email")
    item_name = request.args.get("item_name")

    organization_id = request.args.get("organization_id")
    column = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit")
    # TODO search-3 append like filter for donor_firstname if provided
    if fn:
        query += " AND donor_firstname LIKE %(fn)s"
        args["fn"] = f"%{fn}%"
    # TODO search-4 append like filter for donor_lastname if provided
    if ln:
        query += " AND donor_lastname LIKE %(ln)s"
        args["ln"] = f"%{ln}%"
    # TODO search-5 append like filter for donor_email if provided
    if email:
        query += " AND donor_email LIKE %(email)s"
        args["email"] = f"%{email}%"
    # TODO search-6 append like filter for item_name if provided
    if item_name:
        query += " AND item_name LIKE %(item_name)s"
        args["item_name"] = f"%{item_name}%"
    # TODO search-7 append equality filter for organization_id if provided
    if organization_id:
        query += " AND organization_id LIKE %(organization_id)s"
        args["organization_id"] = f"%{organization_id}%"
    # TODO search-8 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)
    if column and order and column in allowed_columns and order in ("asc", "desc"):
        if column == 'created':
            column = 'donation.created'
        if column == 'modified':
            column = 'donation.modified'
        query += f" ORDER BY {column} {order}"
    # TODO search-9 append limit (default 10) or limit greater than 1 and less than or equal to 100
    if limit:
        try:
            limit = int(limit)
            if 1 < limit <= 100:
                limit = limit
            else:
                limit = 10
                flash("Limit must be between 2 and 100", "error")
        except ValueError:
            limit = 10
            flash("Limit must be a valid number", "error")
    # TODO search-10 provide a proper error message if limit isn't a number or if it's out of bounds
    if not limit:
        limit = 10 # TODO change this per the above requirements
    
    query += " LIMIT %(limit)s"
    args["limit"] = limit
    #print("query",query)
    #print("args", args)
    try:
        result = DB.selectAll(query, args)
        if result.status:
            rows = result.rows
            #print(f"rows: {rows}")
    except Exception as e:
        # TODO search-11 make message user friendly
        flash("Database Search Failed", "error")
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation
    allowed_columns_for_template = [(column, column.replace("_", " ").title()) for column in allowed_columns]
    # TODO search-12 if request args has organization identifier set organization_name variable to the correct name
    
    return render_template("list_donations.html", organization_name=organization_name, rows=rows, allowed_columns=allowed_columns_for_template)


@donations.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description, item_quantity, donation_date, comments
        # TODO add-2 donor_firstname is required (flash proper error message)
        # TODO add-3 donor_lastname is required (flash proper error message)
        # TODO add-4 donor_email is required (flash proper error message)
        # TODO add-4a email must be in proper format (flash proper message)
        # TODO add-5 organization_id is required (flash proper error message)
        # TODO add-6 item_name is required (flash proper error message)
        # TODO add-7 item_description is optional
        # TODO add-8 item_quantity is required and must be more than 0 (flash proper error message)
        # TODO add-9 donation_date is required and must be within the past 30 days
        # TODO add-10 comments are optional
        has_error = False # use this to control whether or not an insert occurs
        

        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO ...
                """, ...
                ) # <-- TODO add-11 add query and add arguments
                if result.status:
                    #print("donation record created")
                    flash("Created Donation Record", "success")
            except Exception as e:
                # TODO add-7 make message user friendly
                #print(f"insert error {e}")
                flash(str(e), "danger")
    return render_template("manage_donation.html",donation=request.form)

@donations.route("/edit", methods=["GET", "POST"])
def edit():
    row = {}
    
    # TODO edit-1 request args id is required (flash proper error message)
    id = False
    if not id: # TODO update this for TODO edit-1
        pass
    else:
        if request.method == "POST":
            
            # TODO add-2 retrieve form data for donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description, item_quantity, donation_date, comments
            # TODO add-3 donor_firstname is required (flash proper error message)
            # TODO add-4 donor_lastname is required (flash proper error message)
            # TODO add-5 donor_email is required (flash proper error message)
            # TODO add-5a email must be in proper format (flash proper message)
            # TODO add-6 organization_id is required (flash proper error message)
            # TODO add-7 item_name is required (flash proper error message)
            # TODO add-8 item_description is optional
            # TODO add-9 item_quantity is required and must be more than 0 (flash proper error message)
            # TODO add-10 donation_date is required and must be within the past 30 days
            # TODO add-11 comments are optional
            has_error = False # use this to control whether or not an insert occurs
                
            if not has_error:
                try:
                    # TODO edit-12 fill in proper update query
                    result = DB.update("""
                    UPDATE ... SET
                    ...
                    """, ...)
                    
                    if result.status:
                        flash("Updated record", "success")
                except Exception as e:
                    # TODO edit-13 make this user-friendly
                    #print(f"update error {e}")
                    flash(e, "danger")
        
        try:
            # TODO edit-14 fetch the updated data 
            result = DB.selectOne("""SELECT 
            ...
            FROM ... LEFT JOIN ... 

            WHERE ..."""
            , id)
            
            if result.status:
                row = result.row
        except Exception as e:
            # TODO edit-15 make this user-friendly
            flash(str(e), "danger")
    
    return render_template("manage_donation.html", donation=row)

@donations.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 if id is missing, flash necessary message and redirect to search
    # TODO delete-2 delete donation by id (fetch the id from the request)
    # TODO delete-3 ensure a flash message shows for successful delete
    # TODO delete-4 pass all argument except id to this route
    # TODO delete-5 redirect to donation search
    pass

    # return redirect(url_for("donations.search", **args))