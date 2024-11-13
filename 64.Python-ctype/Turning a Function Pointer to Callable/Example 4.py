from llvm.core import Module, Function, Type, Builder

mod = Module.new('example')
f = Function.new(mod, Type.function(
				Type.double(), [Type.double(), Type.double()], False), 'foo')

block = f.append_basic_block('entry')
builder = Builder.new(block)

x2 = builder.fmul(f.args[0], f.args[0])
y2 = builder.fmul(f.args[1], f.args[1])

r = builder.fadd(x2, y2)
builder.ret(r)
