import os
import shutil


class Mytempdir:
    """ При входе в контекст создается директория с уникальным именем.
        Вся дальнейшая работа ведется в этой директории (она становится текущей).
        При выходе из контекста директория удаляется вместе со всеми файлами в ней.
        Рабочей директорией становиться та, что была до входа в контекст.
    """

    def __init__(self, name_dir):
        self.old_dir = os.getcwd()
        self.new_dir = os.path.join(self.old_dir, name_dir)

    def __enter__(self):
        if not os.path.exists(self.new_dir):
            os.makedirs(self.new_dir)
        else:
            raise Exception("Folder is already excisted")
        os.chdir(self.new_dir)
        return self.new_dir

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.old_dir)
        try:
            shutil.rmtree(self.new_dir)
        except Exception as ex:
            print(f"Error while deleting folder: {ex}")


if __name__ == "__main__":
    with Mytempdir("new_folder_py") as mt:
        print(f"I am in {os.getcwd()}")
        os.makedirs(os.path.join(os.getcwd(), "new/new/new"))
        os.chdir(os.path.join(os.getcwd(), "new/new/new"))
        print(f"I am in {os.getcwd()}")
    print(f"Now I am in {os.getcwd()}")
    new_dir = os.path.join(os.getcwd(), "new_folder_py")
    print(f"ls: {os.listdir()}")
