

def converter_para_float(valor_str):
    try:
        numero_float = float(valor_str)
        return numero_float
        
    except ValueError:
        return None
    
        