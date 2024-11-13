# Create the trainer and evaluator
def create_supervised_trainer(model, optimizer, loss_fn, device=None):
    if device:
        model.to(device)
    def _update(engine, batch):
        model.train()
        optimizer.zero_grad()
        inputs, targets = batch
        inputs, targets = inputs.view(-1, 784).to(device), targets.to(device)
        outputs = model(inputs)
        loss = loss_fn(outputs, targets)
        loss.backward()
        optimizer.step()
        return loss.item()
    return Engine(_update)

def create_supervised_evaluator(model, metrics, device=None):
    if device:
        model.to(device)
    def _inference(engine, batch):
        model.eval()
        with torch.no_grad():
            inputs, targets = batch
            inputs, targets = inputs.view(-1, 784).to(device), targets.to(device)
            outputs = model(inputs)
            return outputs, targets
    engine = Engine(_inference)
    for name, metric in metrics.items():
        metric.attach(engine, name)
    return engine

trainer = create_supervised_trainer(model, optimizer, loss_fn)
evaluator = create_supervised_evaluator(model, {"accuracy": Accuracy()})
