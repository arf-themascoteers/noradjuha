from fold_evaluator import FoldEvaluator

if __name__ == "__main__":
    inputs = ["bands",
              "props_ex_som",
              "all_ex_som"
              ]
    scenes = [
        "S2B_MSIL2A_20220413T002709_N0400_R016_T54HWE_20220413T021511"
    ]

    configs = []
    for i in inputs:
        configs.append({"input": i, "scenes": scenes})
    c = FoldEvaluator(configs=configs, prefix="all", folds=10, algorithms=["mlr","svr","ann"])
    c.process()