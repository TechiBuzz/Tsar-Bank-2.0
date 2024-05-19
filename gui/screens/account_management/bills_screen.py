from gui.screens.account_management.base_feature_screen import BaseFeatureScreen
import customtkinter as ctk


class BillManagementScreen(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)

        self.app_instance = parent

        self.db_connection = parent.db_connection
        self.account = None

        # Widgets
        BaseFeatureScreen(self, self.app_instance, 'Manage Bills', False)

    def get_name(self) -> str:
        return 'BillManagementScreen'

    def clear_screen(self) -> None:
        self.place_forget()