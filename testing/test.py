#Configuration1
colTargets = {
  "M1": ["A1", "A2"],
  "M2": ["A1", "A3"],
}

def targets(origin: str):
    response = colTargets.get(origin)
      
    return response

print(targets("M2"))