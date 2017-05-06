# H1 odoo
## make an own apps open academy

### it is a tutorial

some issues:
    1. sometimes i have stop whole odoo server to reinstall this apps
    2. upgrade has no effect after having changes in models.py, only a reinstall works
    3. after add session model, upgrade has no effect
    4. after changing openacademy.xml, there are errors: "Model not found: openacademy.session"
    5. after restarting odoo server, the errors are gone. Cool!
    6. adding many2one relation on model. maybe need stop odoo server again to see the effect.
    7. install failed after loading xml, try exclude openacademy in manifest, no effect.  delete openacademy from addons ! then relink/ cancel upgrade! i will try unistall and install
