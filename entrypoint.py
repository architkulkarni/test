import ray
ray.init(runtime_env={"pip": ["flash-attn==2.3.6"]})

# Launch a task
@ray.remote
def f():
    print("Successfully installed flash-attn==2.3.6")

ray.get(f.remote())