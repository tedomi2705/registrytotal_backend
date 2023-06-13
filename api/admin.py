from django.contrib import admin
from .models import Inspection, InspectionCenter, InspectionRecord, Owner, Upload, User, Vehicle

class InspectionAdmin(admin.ModelAdmin):
    list_display = ('inspection_id', 'certificate_no', 'expiration_date', 'inspected_by', 'inspection_date', 'vehicle_id', 'owner_id')
admin.site.register(Inspection, InspectionAdmin)

class InspectionCenterAdmin(admin.ModelAdmin):
    list_display = ('center_id', 'center_name', 'province', 'user_id')
admin.site.register(InspectionCenter, InspectionCenterAdmin)

class InspectionRecordAdmin(admin.ModelAdmin):
    list_display = ('record_id', 'result', 'center_id', 'inspection_id')
admin.site.register(InspectionRecord, InspectionRecordAdmin)

class OwnerAdmin(admin.ModelAdmin):
    list_display = ('owner_id', 'owner_info', 'owner_type', 'province')
admin.site.register(Owner, OwnerAdmin)

class UploadAdmin(admin.ModelAdmin):
    list_display = ('upload_id', 'file_name', 'file_size', 'upload_date', 'center_id')
admin.site.register(Upload, UploadAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'email', 'password', 'user_type')
    list_filter = ('email', 'user_type')
admin.site.register(User, UserAdmin)

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_id', 'manufacturer', 'model', 'plate_no', 'province', 'registration_cert_no')
admin.site.register(Vehicle, VehicleAdmin)

