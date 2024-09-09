def get_model_path():
    import os 
    my_path = __file__
    print(my_path)
    dir_name = os.path.dirname(my_path)
    model_path = os.path.join(dir_name, "lr_model.pkl")

    return model_path
