# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdminMaster(models.Model):
    deptid = models.IntegerField(db_column='deptId', primary_key=True)  # Field name made lowercase.
    deptname = models.CharField(db_column='deptName', max_length=150)  # Field name made lowercase.
    departshortname = models.CharField(db_column='departShortName', max_length=100)  # Field name made lowercase.
    departcode = models.CharField(db_column='departCode', max_length=50)  # Field name made lowercase.
    empid = models.IntegerField(db_column='empId', blank=True, null=True)  # Field name made lowercase.
    roleid = models.IntegerField(db_column='roleId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin_master'


class Admintable(models.Model):
    adminid = models.AutoField(db_column='adminId', primary_key=True)  # Field name made lowercase.
    username = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=30, blank=True, null=True)
    updatedate = models.DateTimeField(db_column='updateDate', blank=True, null=True)  # Field name made lowercase.
    empid = models.IntegerField(db_column='empId', blank=True, null=True)  # Field name made lowercase.
    roleid = models.ForeignKey('RoleMaster', models.DO_NOTHING, db_column='roleId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admintable'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DepartmentMaster(models.Model):
    deptid = models.AutoField(db_column='deptId', primary_key=True)  # Field name made lowercase.
    deptname = models.CharField(db_column='deptName', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'department_master'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EmployeeTable(models.Model):
    empid = models.AutoField(db_column='empId', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    middlename = models.CharField(db_column='middleName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='emailId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    dob = models.DateField()
    address = models.CharField(max_length=255, blank=True, null=True)
    phoneno = models.CharField(db_column='phoneNo', max_length=11, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(max_length=30, blank=True, null=True)
    deptid = models.ForeignKey(DepartmentMaster, models.DO_NOTHING, db_column='deptId', blank=True, null=True)  # Field name made lowercase.
    roleid = models.ForeignKey('RoleMaster', models.DO_NOTHING, db_column='roleId', blank=True, null=True)  # Field name made lowercase.
    updatedate = models.DateField(db_column='updateDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employee_table'


class Employeeleavebalance(models.Model):
    empleavebalanceid = models.AutoField(db_column='empLeaveBalanceId', primary_key=True)  # Field name made lowercase.
    leavebalance = models.DecimalField(db_column='leaveBalance', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    empid = models.ForeignKey(EmployeeTable, models.DO_NOTHING, db_column='empId', blank=True, null=True)  # Field name made lowercase.
    leavetypeid = models.ForeignKey('LeavetypesMaster', models.DO_NOTHING, db_column='leaveTypeId', blank=True, null=True)  # Field name made lowercase.
    quarter = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'employeeleavebalance'


class LeaverequestTable(models.Model):
    leaverequestid = models.AutoField(db_column='leaveRequestId', primary_key=True)  # Field name made lowercase.
    leavetypeid = models.ForeignKey('LeavetypesMaster', models.DO_NOTHING, db_column='leaveTypeId', blank=True, null=True)  # Field name made lowercase.
    empleavebalanceid = models.ForeignKey(Employeeleavebalance, models.DO_NOTHING, db_column='empLeaveBalanceId', blank=True, null=True)  # Field name made lowercase.
    fromdate = models.DateField(db_column='fromDate', blank=True, null=True)  # Field name made lowercase.
    todate = models.DateField(db_column='toDate', blank=True, null=True)  # Field name made lowercase.
    noofdayleave = models.DecimalField(db_column='noOfDayLeave', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    applieddate = models.DateField(db_column='appliedDate', blank=True, null=True)  # Field name made lowercase.
    leavestatusid = models.ForeignKey('LeavestatusMaster', models.DO_NOTHING, db_column='leaveStatusId', blank=True, null=True)  # Field name made lowercase.
    adminremark = models.TextField(db_column='adminRemark', blank=True, null=True)  # Field name made lowercase.
    adminremarkdate = models.DateField(db_column='adminRemarkDate', blank=True, null=True)  # Field name made lowercase.
    empid = models.ForeignKey(EmployeeTable, models.DO_NOTHING, db_column='empId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'leaverequest_table'


class LeavestatusMaster(models.Model):
    leavestatusid = models.AutoField(db_column='leaveStatusId', primary_key=True)  # Field name made lowercase.
    leavestatus = models.CharField(db_column='leaveStatus', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'leavestatus_master'


class LeavetypesMaster(models.Model):
    leavetypeid = models.AutoField(db_column='leaveTypeId', primary_key=True)  # Field name made lowercase.
    leavetype = models.CharField(db_column='leaveType', max_length=200, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'leavetypes_master'


class RoleMaster(models.Model):
    roleid = models.AutoField(db_column='roleId', primary_key=True)  # Field name made lowercase.
    rolename = models.CharField(db_column='roleName', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'role_master'


class Tblemployees(models.Model):
    empid = models.AutoField(db_column='empId', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='emailId', max_length=200, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(max_length=180, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=150, blank=True, null=True)
    phonenumber = models.CharField(db_column='phoneNumber', max_length=11, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=50, blank=True, null=True)
    updationdate = models.DateTimeField(db_column='updationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblemployees'


class Tblleavesenctiondescription(models.Model):
    leavesanctionid = models.AutoField(db_column='leaveSanctionId', primary_key=True)  # Field name made lowercase.
    description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblleavesenctiondescription'


class Tbluser(models.Model):
    userid = models.AutoField(db_column='userId', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(max_length=100, blank=True, null=True)
    updationdate = models.DateTimeField(db_column='updationDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbluser'
