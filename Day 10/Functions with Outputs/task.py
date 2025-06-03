def format_name(f_name, l_name):
    titled_F_name = f_name.title()
    titled_L_name = l_name.title()
    return f"Nome: {titled_F_name} \nSobrenome: {titled_L_name}"

nomeFormatado = format_name("jOAo gabRIEl", "OliveRIa")
print(nomeFormatado)