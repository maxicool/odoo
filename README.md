## odoo
## make an own apps open academy

### it is a tutorial

#### some issues:

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
11. add couse name, instructors to ession tree/list view
