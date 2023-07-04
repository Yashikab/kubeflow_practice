from kfp import compiler

def compile_to_yaml(target_pipeline, package_path="pipeline.yaml"):
    compiler.Compiler().compile(target_pipeline, package_path)
