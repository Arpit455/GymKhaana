from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    # Base Link
    
    path('', views.HomePage, name='home-page'),

    # Registration Based Links

    path('login/', auth_views.LoginView.as_view(), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), {'template_name': 'gymnasium/home.html'}, name='logout'),

    path('change-password/', views.changePassword, name='change-password'),

    # General Outer Website Links

    path('aquatics/', views.Aquatics, name='aquatics'),

    path('view-announcements/', views.DisplayAnnouncements, name='view-announcements'),

    # Customer Website Links

    path('customer-profile/', views.DisplayCustomerProfile, name='customer-profile'),

    path('edit-customer-profile/', views.ChangeCustomerProfile, name='edit-customer-profile'),

    path('view-notifications/', views.DisplayCustomerNotification, name='display-notification'),

    # Trainer Website Links

    path('trainer-profile/', views.DisplayTrainerProfile, name='trainer-profile'),

    path('edit-trainer-profile/', views.ChangeTrainerProfile, name='edit-trainer-profile'),

    # Manager Website Links

    path('manager-profile/', views.DisplayManagerProfile, name='manager-profile'),

    path('edit-manager-profile/', views.ChangeManagerProfile, name='edit-manager-profile'),

    path('view-customer-list/', views.DisplayCustomerList, name='view-customer-list'),

    path('view-customer/<int:cust_id>/', views.DisplayIndividualCustomer, name='view-individual-customer'),

    path('view-trainer-list/', views.DisplayTrainerList, name='view-trainer-list'),

    path('view-trainer/<int:tra_id>/', views.DisplayIndividualTrainer, name='view-individual-trainer'),

    path('view-manager-list/', views.DisplayManagerList, name='view-manager-list'),

    path('view-manager/<int:man_id>/', views.DisplayIndividualManager, name='view-individual-manager'),

    path('view-admin-list/', views.DisplayAdminList, name='view-admin-list'),

    path('view-admin/<int:adm_id>/', views.DisplayIndividualAdmin, name='view-individual-admin'),

    path('view-all-announcements/', views.DisplayAnnouncementList, name='view-all-announcements'),

    path('edit-announcement/<int:ann_id>/', views.EditIndividualAnnouncement, name='edit-announcement'),

    path('post-announcement/', views.PostAnnouncement, name='post-announcement'),

    path('delete-announcement/<int:ann_id>/', views.DeleteIndividualAnnouncement, name='delete-announcement'),

    path('view-all-equipment-types/', views.DisplayEquipmentTypeList, name='view-all-equipment-types'),

    path('edit-equipment-type/<int:eqty_id>/', views.EditEquipmentType, name='edit-equipment-type'),

    path('create-equipment-type/', views.CreateEquipmentType, name='create-equipment-type'),

    path('delete-equipment-type/<int:eqty_id>/', views.DeleteEquipmentType, name='delete-equipment-type'),

    # Links common to Manager and Trainer

    path('view-all-notifications/', views.DisplayNotificationList, name='view-my-notifications'),

    path('edit-notification/<int:not_id>/', views.EditIndividualNotification, name='edit-notification'),

    path('post-notification/', views.PostNotification, name='post-notification'),

    path('delete-notification/<int:not_id>/', views.DeleteIndividualNotification, name='delete-notification'),

]