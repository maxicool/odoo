## odoo to create an own apps - open academy

### my work log:

1. sometimes i have stop whole odoo server to reinstall this apps
2. upgrade has no effect after having changes in models.py, only a reinstall works
3. after add session model, upgrade has no effect
4. after changing openacademy.xml, there are errors: "Model not found: openacademy.session"
5. after restarting odoo server, the errors are gone. Cool!
6. adding many2one relation on model. maybe need stop odoo server again to see the effect.
7. install failed after loading xml, try exclude openacademy in manifest, no effect.  delete openacademy from addons ! then relink/ cancel upgrade! i will try unistall and install
8. changed model add instructor. i will not change xml file first. still try upgrading first.
9. add tree view for course! and found bug from official tutorial:

postgres table description
```
\d+ openacademy_course;
```
| Column | Type |
| --- | --- |
| id| Integer|
| responsible| Integer|

```xml
<record model="ir.ui.view" id="course_tree_view">
    <field name="name">course.tree</field>
    <field name="model">openacademy.course</field>
    <field name="arch" type="xml">
        <tree string="Course Tree">
            <field name="name"/>
            <!--  <field name="responsible_id"/>  original from tutorial
                but responsible_id not in openacademy.course
            -->
            <field name="responsible"/>
        </tree>
    </field>
</record>
```
10. add instructor_id and course_id to xml. todo: add search view for session. people can find course /session by instructors.
11. add course name, instructors to session tree/list view
12. add Many2many for attendees in models then upgrade!
13. add Many2many in xml! no errors
14. working on inheritance
  * add partner.py in models following by tutorial. but maybe i should modify _\_\_init\_\_.py_ by adding from models import ...
  * add partner.xml upgrade and see （wow! no errors)
  * add relation for instructors and session in partner.py
15. working with domain and conditions.
16. Computed fields and progressbar
17. Default value
18. onchange (change model, odoo need to be restarted)
19. model constraints
  * python constraints
  * SQL constraints
20. Calendar view (no effect)
21. Search views (Groupby ui is cute)
22. Gantt charts
23. Graph views
24. Kanban
25. Workflow
  * workflow like object/button
  * workflow + automatic workflow (at home workflow works not same as in the office, even the code is same, delete sessions, it works now)
  * server's action instead of python code
26. security （no real code)
27. wizard: wizard is in action menu :-)
