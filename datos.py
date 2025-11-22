parametros_generales = {
    "apresupuesto": 450_000_000,  # US$
    "d%Aumento": 0.0339,  # 3.39% kWh/año
    "demanda_electrica_año_inicial": 158_314_691  # kWh/año
}

# Parámetros por tecnología (usando índices numéricos para coincidir con J)
tecnologias = {
    0: {  # Panel solar pequeño
        "e_j": 1000, # Área requerida en m2
        "p_j": 941 * 100, # Precio por Kw instalado * Capacidad maxima
        "c_j": 40 * (1_327_000//1000), # (Kg CO2/kWh) * KWh producido 
        "hvida_j": 30, # Vida útil en años
        "v%guardar_j": 0.60, # Porcentaje de energía que se puede guardar
        "b_j": 0, 
        "vdis_j": 0
    },
    1: {  # Panel solar grande
        "e_j": 106_700, # Área requerida en m2
        "p_j": 771 * 3000, # Precio por Kw instalado * Capacidad maxima 
        "c_j": 40 * 13_271_000//1000, #(Kg CO2/kWh) * KWh producido 
        "hvida_j": 30, # Vida útil en años
        "v%guardar_j": 0.50,  # Porcentaje de energía que se puede guardar
        "b_j": 0,
        "vdis_j": 0
    },
    2: {  # Molino eolico pequeño
        "e_j": 162000, # Área requerida en m2
        "p_j": 1222 * 1500, # Precio por Kw instalado * Capacidad maxima
        "c_j": 5.3 * 3_500_000//1000,  #(Kg CO2/kWh) * KWh producido
        "hvida_j": 30, # Vida útil en años
        "v%guardar_j": 0.50, # Porcentaje de energía que se puede guardar
        "b_j": 0, 
        "vdis_j": 500 # Distancia minima a casas
    },
    3: {  # Molino eolico grande
        "e_j": 25_250, 
        "p_j": 1494 * 5000, 
        "c_j": 5.3 * 17_000_000//1000, 
        "hvida_j": 25,
        "v%guardar_j": 0.40, 
        "b_j": 0, 
        "vdis_j": 500
    },
    4: {  # Bateria litio
        "e_j": 0.3, # Área requerida en m2
        "p_j": 1556, # Precio por Kw instalado
        "c_j": 168000, # (KwCO2/kWh)
        "hvida_j": 20, # Vida útil en años
        "v%guardar_j": 0.00, 
        "b_j": 230 # Almacenamiento en kWh
    },
    5: {  # Bateria plomo-acido
        "e_j": 5.74, 
        "p_j": 1100, 
        "c_j": 175_000 * 1.2, #kwCO2/kWh
        "hvida_j": 15,
        "v%guardar_j": 0.00, 
        "b_j": 1.2
    },
    6: {  # Bateria flujo
        "e_j": 13.74, 
        "p_j": 1700, 
        "c_j": 183000 * 800, 
        "hvida_j": 20,
        "v%guardar_j": 0.00, 
        "b_j": 800
    }
}

# Parámetros por ubicación (usando índices numéricos para coincidir con K)
ubicaciones = {
    0: {  # Poniente
        "parriendo_k": 3160, "t_area_k": 500_000, "t_hogares_k": 500 # Terrenos usan mismo area asi que se usara uno
    },
    1: {  # Oriente
        "parriendo_k": 2186, "t_area_k": 500_000, "t_hogares_k": 500
    }
}

# Producción energética por tecnología y ubicación (w_j,k)
produccion_energia = { # k= 
    0: {0: 1_327_000, 1: 1_327_000},        # Panel solar pequeño
    1: {0: 13_271_000, 1: 39_814_000},      # Panel solar grande  
    2: {0: 3_500_000, 1: 2_750_000},        # Molino eolico pequeño
    3: {0: 17_000_000, 1: 13_500_000}       # Molino eolico grande
}

# Eficiencia por tecnología y condición climática (y_j,z)
eficiencia_climatica = {
    0: {"Viento bajo/Nublado": 0.3325, "Viento medio/Parcialmente nublado": 0.762, "Mucho viento/Soleado": 1.0},
    1: {"Viento bajo/Nublado": 0.3325, "Viento medio/Parcialmente nublado": 0.762, "Mucho viento/Soleado": 1.0},
    2: {"Viento bajo/Nublado": 0.3, "Viento medio/Parcialmente nublado": 0.6, "Mucho viento/Soleado": 1.0},
    3: {"Viento bajo/Nublado": 0.55, "Viento medio/Parcialmente nublado": 0.8, "Mucho viento/Soleado": 1.0},
    4: {"Viento bajo/Nublado": 1.0, "Viento medio/Parcialmente nublado": 1.0, "Mucho viento/Soleado": 1.0},
    5: {"Viento bajo/Nublado": 1.0, "Viento medio/Parcialmente nublado": 1.0, "Mucho viento/Soleado": 1.0},
    6: {"Viento bajo/Nublado": 1.0, "Viento medio/Parcialmente nublado": 1.0, "Mucho viento/Soleado": 1.0}
}

# Parámetros climáticos (α_z) y mapeo de días de la semana
dias_semana = {
    0: {"condicion": "Viento bajo/Nublado", "alpha_z": 481442.96},
    1: {"condicion": "Viento medio/Parcialmente nublado", "alpha_z": 449786.83},
    2: {"condicion": "Mucho viento/Soleado", "alpha_z": 421593.05},
    3: {"condicion": "Viento medio/Parcialmente nublado", "alpha_z": 449786.83},
    4: {"condicion": "Viento bajo/Nublado", "alpha_z": 481442.96},
    5: {"condicion": "Mucho viento/Soleado", "alpha_z": 421593.05},
    6: {"condicion": "Mucho viento/Soleado", "alpha_z": 421593.05}
}
