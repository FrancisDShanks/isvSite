# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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


class IsvComments(models.Model):
    id = models.CharField(primary_key=True, max_length=1024)
    url = models.CharField(max_length=1024, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    post_id = models.CharField(max_length=1024, blank=True, null=True)
    html_url = models.CharField(max_length=1024, blank=True, null=True)
    official = models.NullBooleanField()
    vote_sum = models.IntegerField(blank=True, null=True)
    author_id = models.CharField(max_length=1024, blank=True, null=True)
    created_at_timestamp = models.FloatField(blank=True, null=True)
    created_at_str = models.CharField(max_length=1024, blank=True, null=True)
    updated_at_timestamp = models.FloatField(blank=True, null=True)
    updated_at_str = models.CharField(max_length=1024, blank=True, null=True)
    vote_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'isv_comments'


class IsvCommentsJson(models.Model):
    jdoc = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'isv_comments_json'


class IsvPosts(models.Model):
    id = models.CharField(primary_key=True, max_length=1024)
    url = models.CharField(max_length=1024, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    closed = models.NullBooleanField()
    pinned = models.NullBooleanField()
    status = models.CharField(max_length=1024, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    featured = models.NullBooleanField()
    html_url = models.CharField(max_length=1024, blank=True, null=True)
    topic_id = models.CharField(max_length=1024, blank=True, null=True)
    vote_sum = models.IntegerField(blank=True, null=True)
    author_id = models.CharField(max_length=1024, blank=True, null=True)
    created_at_timestamp = models.FloatField(blank=True, null=True)
    created_at_str = models.CharField(max_length=1024, blank=True, null=True)
    updated_at_timestamp = models.FloatField(blank=True, null=True)
    updated_at_str = models.CharField(max_length=1024, blank=True, null=True)
    vote_count = models.IntegerField(blank=True, null=True)
    comment_count = models.IntegerField(blank=True, null=True)
    follower_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'isv_posts'


class IsvPostsJson(models.Model):
    jdoc = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'isv_posts_json'


class IsvTopics(models.Model):
    id = models.CharField(primary_key=True, max_length=1024)
    url = models.CharField(max_length=1024, blank=True, null=True)
    html_url = models.CharField(max_length=1024, blank=True, null=True)
    name = models.CharField(max_length=1024, blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)
    position = models.CharField(max_length=1024, blank=True, null=True)
    follower_count = models.CharField(max_length=1024, blank=True, null=True)
    community_id = models.CharField(max_length=1024, blank=True, null=True)
    created_at = models.CharField(max_length=1024, blank=True, null=True)
    updated_at = models.CharField(max_length=1024, blank=True, null=True)
    user_segment_id = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'isv_topics'


class IsvUsers(models.Model):
    id = models.CharField(primary_key=True, max_length=1024)
    url = models.CharField(max_length=1024, blank=True, null=True)
    name = models.CharField(max_length=1024, blank=True, null=True)
    email = models.CharField(max_length=1024, blank=True, null=True)
    created_at = models.CharField(max_length=1024, blank=True, null=True)
    updated_at = models.CharField(max_length=1024, blank=True, null=True)
    time_zone = models.CharField(max_length=1024, blank=True, null=True)
    phone = models.CharField(max_length=1024, blank=True, null=True)
    shared_phone_number = models.CharField(max_length=1024, blank=True, null=True)
    photo = models.TextField(blank=True, null=True)
    locale_id = models.CharField(max_length=1024, blank=True, null=True)
    locale = models.CharField(max_length=1024, blank=True, null=True)
    organization_id = models.CharField(max_length=1024, blank=True, null=True)
    role = models.CharField(max_length=1024, blank=True, null=True)
    verified = models.NullBooleanField()
    result_type = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'isv_users'


class ZendeskUserInfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)

    class Meta:
        managed = True
        db_table = 'zendesk_userinfo'


class DBUpdateTime(models.Model):
    timestamp = models.CharField(primary_key=True, max_length=32)
    date = models.CharField(max_length=32)
    time = models.CharField(max_length=32)

    class Meta:
        managed = True
        db_table = 'isv_update'
