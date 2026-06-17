# Realizar a aplicação no google colab ou no python fiddle

import pandas as pd

varejo = ['Abacate', 'Abacaxi', 'Açaí', 'Acerola', 'Ameixa', 'Amora', 'Ananás', 'Atemoia', 'Avelã', 'Babaco',
    'Bacuí', 'Bacuri', 'Banana', 'Baru', 'Bergamota', 'Beringela', 'Bilimbi', 'Biribá', 'Buriti', 'Cacau',
    'Cagaita', 'Caju', 'Calamansi', 'Cambucá', 'Cambuci', 'Camu-camu', 'Carambola', 'Cariota', 'Castanha', 'Caviar-cítrico',
    'Cereja', 'Cidra', 'Ciriguela', 'Coco', 'Cranberry', 'Cupuaçu', 'Damasco', 'Dendê', 'Durião', 'Embaúba',
    'Figo', 'Framboesa', 'Fruta-pão', 'Gabiroba', 'Glicosmis', 'Goiaba', 'Granadilla', 'Groselha', 'Grumixama', 'Guabiju',
    'Guaraná', 'Guariroba', 'Ilama', 'Inajá', 'Ingá', 'Jabuticaba', 'Jaca', 'Jambo', 'Jambolão', 'Jaracatiá',
    'Jatobá', 'Jenipapo', 'Jerivá', 'Juçara', 'Kiwano', 'Kiwi', 'Laranja', 'Laranja-kinkan', 'Lichia', 'Lima',
    'Limão', 'Longan', 'Lucuma', 'Macaúba', 'Maçã', 'Mamão', 'Manga', 'Mangaba', 'Maracujá', 'Marang',
    'Marmelo', 'Melancia', 'Melão', 'Mirtilo', 'Morango', 'Murici', 'Nectarina', 'Nêspera', 'Noz', 'Pequi',
    'Pêra', 'Pêssego', 'Physalis', 'Pitanga', 'Pitaya', 'Romã', 'Tamarindo', 'Tangerina', 'Uva', 'Uvaia']

df_varejo = pd.DataFrame(varejo, columns = ['Frutas'])
print(df_varejo)
