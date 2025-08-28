from attack.run import rsi_runner

if __name__ == "__main__":
    model_types = ["resnet34" ]
    for model in model_types:
        rsi_runner(model)
 
