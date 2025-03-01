import inspect
import os
import imp


class Models:

    def __init__(self):
        self.path_models = []
        self.model_names = []
        self.GetModelPath()
        self.get_class_from_modules(self.path_models)

    # 获取神经元模型所在文件夹路径以及每个模型文件的文件路径
    def GetModelPath(self):
        relative_path = os.path.dirname(os.path.dirname(__file__))
        path_models = os.path.join(relative_path, 'models')

        for root, dirs, files in os.walk(path_models):
            for file in files:
                if file.endswith('.py') and 'model' in file:
                    path = os.path.join(root, file)
                    self.model_names.append(file)
                    self.path_models.append(path)

    def get_class_from_modules(self, module_list):
        """
        可以使用inspect直接根据module拿到其中所有的类
        :param module_list:
        :return:
        """
        class_list = []
        for module in self.path_models:
            for name, obj in inspect.getmembers(module, inspect.isclass):
                # class_list[name] = obj
                print(name, obj)


if __name__ == '__main__':
    Models = Models()
