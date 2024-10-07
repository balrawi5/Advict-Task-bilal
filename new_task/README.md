Overview:
    This module extends Odoo's product, sales, and invoicing functionalities by adding custom fields and logic for managing warranties. It also includes a warranty report and an automated email notification system to remind customers about warranty expiry.

Features:
    - Product Customization: Adds warranty period and manufacturer fields to the product form.
    - Sale Order Customization: Automatically populates the warranty period on sale order lines based on the selected product.
    - Invoice Customization: Calculates and displays the warranty expiry date on customer invoices.
    - Warranty Report: Lists sale orders along with their warranty expiry dates, with filters for products and customers.
    - Warranty Expiry Notifications: Automatically sends an email reminder to customers 30 days before their warranty expires.

Installation:
    1. download the module into your Odoo addons directory
    2. restart the Odoo server
    3. Activate Developer Mode:
        - Go to Settings > Activate Developer Mode.
    4. Install the module:
        - Navigate to Apps.
        - Search for Task module.
        - Click Activate.

Usage:

    After installing the module, go to:
        1. Product Customization:
            A. Sales > Products > Product Variants.
            B. You will find the new field (warranty_period, manufacturer) in the tree list.
            C. select any product and scroll to the new Fields Added in the form of product.product model.
        
        2. Sale Order Line Customization:
            A. Sales > Orders > Quotations.
            B. Create a new order by click on New button
            C. Add a product with a warranty. The warranty_period will be automatically populated based on the product.
            D. You can also manually change the warranty period if needed in sale order line.
        
        3. Invoice Customization:
            A. Navigate to Invoicing menu
            B. The field is displayed in the customer invoice list view and can be viewed in the form view.
            C. The warranty expiry date (warranty_expiry_date) will be automatically calculated based on the warranty period + order create date.

        4. Warranty Report:
            A. Navigate to Sales > Reports > Warranty Report.
            B. The report displays:
                - Sale order number
                - Customer
                - Product
                - Warranty period
                - Warranty expiry date
            C. You can filter the report by customer or product.

        5. Warranty Expiry Notifications:
            A. The module automatically sends an email reminder to customers 30 days before their warranty expires.
            B. The email is sent from the Odoo server and includes the customer's name
            C. To check or manually trigger the scheduled action, navigate to 
                Settings > Technical > Automation > Scheduled Actions 
                search for "Warranty Expiry Notification".
            D. The email template used for notifications is customizable: - Go to 
                Settings > Technical > Email > Emal Templates. 
                - Search for the template named Warranty Expiry Notification. You can modify the email content here.


