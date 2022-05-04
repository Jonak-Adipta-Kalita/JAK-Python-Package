from jak_python_package.api import API

jak_api = API("YOUR_KEY")

# Get JAK
jak_details = jak_api.get_jak()

# Get Brawl Stars
brawl_stars_data = jak_api.get_brawl_stars()

# Get Ben 10
ben10_data = jak_api.get_ben10()

# Get Miraculous
miraculous_data = jak_api.get_miraculous()

# Get Mughal Empire
mughal_empire_data = jak_api.get_mughal_empire()

# Get Genshin Impact
genshin_impact_data = jak_api.get_genshin_impact()

# Get Alexis Response
alexis_reponse = jak_api.get_alexis_response("Hello!!")
