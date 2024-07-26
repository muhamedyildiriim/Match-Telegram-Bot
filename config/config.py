import configparser

class Config:
    def __init__(self, file_path):
        self.config = configparser.ConfigParser()
        self.file_path = file_path
        self.load_config()

    def load_config(self):
        self.config.read(self.file_path)

    def get_section(self, section_name):
        if section_name in self.config:
            return self.config[section_name]
        else:
            raise KeyError(f"'{section_name}' bölümü bulunamadı.")

    def get_full_config(self):
        return self.config
    
