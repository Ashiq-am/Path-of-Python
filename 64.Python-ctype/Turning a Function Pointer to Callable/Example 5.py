from llvm.ee import ExecutionEngine

engine = ExecutionEngine.new(mod)
ptr = engine.get_pointer_to_function(f)
ptr
