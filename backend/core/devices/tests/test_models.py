import pytest
from devices.tests.fixtrues import device



@pytest.mark.django_db
class TestDevicsModels:
    def test_create_model(self,device):
        assert device.id
        assert device.physical_information.id

        assert device.hardware_information.id
        assert device.hardware_information.processor.id
        assert device.hardware_information.graphic_processor.id
        assert device.hardware_information.camera.id
        assert device.hardware_information.display.id

        assert device.software_information.id
        assert device.software_information.operating_system.id

        assert device.category.id
        assert device.features.id
    
    def test_representation(self, device):
        assert str(device) == device.device_name

        assert str(device.physical_information) == f"{device.device_name} Physical Information"

        assert str(device.hardware_information) == f"{device.device_name} Hardware Information"
        assert str(device.hardware_information.camera) == device.hardware_information.camera.description
        assert str(device.hardware_information.processor) == device.hardware_information.processor.processor_name
        assert str(device.hardware_information.graphic_processor) == device.hardware_information.graphic_processor.graphic_proccessor_name
        assert str(device.hardware_information.display) == f"{device.device_name} Display"
        
        assert str(device.software_information) == f"{device.device_name} Software Information"
        assert str(device.software_information.operating_system) == device.software_information.operating_system.os_name
        
        assert str(device.category) == device.category.category_name
        assert str(device.features) == device.features.feature_name

    def test_auto_created_fields(self, device):
        assert device.created_at and device.updated_at
        
        assert device.physical_information.created_at and device.physical_information.updated_at

        assert device.hardware_information.created_at and device.hardware_information.updated_at
        assert device.hardware_information.camera.created_at and device.hardware_information.camera.updated_at
        assert device.hardware_information.processor.created_at and device.hardware_information.processor.updated_at
        assert device.hardware_information.graphic_processor.created_at and device.hardware_information.graphic_processor.updated_at
        assert device.hardware_information.display.created_at and device.hardware_information.display.updated_at

        assert device.software_information.created_at and device.software_information.updated_at
        assert device.software_information.operating_system.created_at and device.software_information.operating_system.updated_at
        
        assert device.category.created_at and device.category.updated_at
        assert device.features.created_at and device.features.updated_at
