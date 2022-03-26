from .views import CreateSecurityMechanismView
from rest_framework.routers import SimpleRouter 
# create router object
router = SimpleRouter()
# register  CreateFileView with router
router.register('', CreateSecurityMechanismView,)


urlpatterns = router.urls