import ray
ray.init(runtime_env={"pip": ["flash-attn==2.3.6"]})
print("Successfully installed flash-attn==2.3.6")