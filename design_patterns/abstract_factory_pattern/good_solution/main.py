# App initialization
from abstract_factory_pattern.good_solution.framework.mac_ui_component_factory import (
    MacUIComponentFactory,
)
from abstract_factory_pattern.good_solution.framework.ui_component_factory import (
    UIComponentFactory,
)
from abstract_factory_pattern.good_solution.framework.windows_ui_component_factory import (
    WindowsUIComponentFactory,
)
from abstract_factory_pattern.good_solution.user_settings_form import (
    UserSettingsForm,
)
from abstract_factory_pattern.naive_solution.gui_framework.operating_system_type import (
    OperatingSystemType,
)

os = OperatingSystemType.MAC  # Example operating system
ui_component_factory: UIComponentFactory

if os == OperatingSystemType.WINDOWS:
    ui_component_factory = WindowsUIComponentFactory()
elif os == OperatingSystemType.MAC:
    ui_component_factory = MacUIComponentFactory()
else:
    raise Exception("Unsupported operating system")

# Render the User Settings Form
UserSettingsForm().render(ui_component_factory)

# Logs:
# Mac: render button
# Mac: render checkbox