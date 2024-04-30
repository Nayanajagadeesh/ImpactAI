def crop(crop_name):
    crop_data = {
    "wheat":["/static/images2/wheat.jpg", "U.P., Punjab, Haryana, Rajasthan, M.P., bihar", "rabi","Sri Lanka, United Arab Emirates, Taiwan"],
    "paddy":["/static/images2/paddy.jpg", "W.B., U.P., Andhra Pradesh, Punjab, T.N.", "kharif","Bangladesh, Saudi Arabia, Iran"],
    "barley":["/static/images2/barley.jpg", "Rajasthan, Uttar Pradesh, Madhya Pradesh, Haryana, Punjab", "rabi","Oman, UK, Qatar, USA"],
    "maize":["/static/images2/maize.jpg", "Karnataka, Andhra Pradesh, Tamil Nadu, Rajasthan, Maharashtra", "kharif", "Hong Kong, United Arab Emirates, France"],
    "bajra":["/static/images2/bajra.jpg", "Rajasthan, Maharashtra, Haryana, Uttar Pradesh and Gujarat", "kharif", "Oman, Saudi Arabia, Israel, Japan"],
    "copra":["/static/images2/copra.jpg", "Kerala, Tamil Nadu, Karnataka, Andhra Pradesh, Orissa, West Bengal","rabi", "Veitnam, Bangladesh, Iran, Malaysia"],
    "cotton":["/static/images2/cotton.jpg", "Punjab, Haryana, Maharashtra, Tamil Nadu, Madhya Pradesh, Gujarat", " China, Bangladesh, Egypt"],
    "masoor":["/static/images2/masoor.jpg", "Uttar Pradesh, Madhya Pradesh, Bihar, West Bengal, Rajasthan", "rabi", "Pakistan, Cyprus,United Arab Emirates"],
    "gram":["/static/images2/gram.jpg", "Madhya Pradesh, Maharashtra, Rajasthan, Uttar Pradesh, Andhra Pradesh & Karnataka", "rabi", "Veitnam, Spain, Myanmar"],
    "groundnut":["/static/images2/groundnut.jpg", "Andhra Pradesh, Gujarat, Tamil Nadu, Karnataka, and Maharashtra", "kharif", "Indonesia, Jordan, Iraq"],
    "arhar":["/static/images2/arhar.jpg", "Maharashtra, Karnataka, Madhya Pradesh and Andhra Pradesh", "kharif", "United Arab Emirates, USA, Chicago"],
    "sesamum":["/static/images2/sesamum.jpg", "Maharashtra, Rajasthan, West Bengal, Andhra Pradesh, Gujarat", "rabi", "Iraq, South Africa, USA, Netherlands"],
    "jowar":["/static/images2/jowar.jpg", "Maharashtra, Karnataka, Andhra Pradesh, Madhya Pradesh, Gujarat", "kharif", "Torronto, Sydney, New York"],
    "moong":["/static/images2/moong.jpg", "Rajasthan, Maharashtra, Andhra Pradesh", "rabi", "Qatar, United States, Canada"],
    "niger":["/static/images2/niger.jpg", "Andha Pradesh, Assam, Chattisgarh, Gujarat, Jharkhand", "kharif", "United States of American,Argenyina, Belgium"],
    "rape":["/static/images2/rape.jpg", "Rajasthan, Uttar Pradesh, Haryana, Madhya Pradesh, and Gujarat", "rabi", "Veitnam, Malaysia, Taiwan"],
    "jute":["/static/images2/jute.jpg", " West Bengal , Assam , Orissa , Bihar , Uttar Pradesh", "kharif", "JOrdan, United Arab Emirates, Taiwan"],
    "safflower":["/static/images2/safflower.jpg",  "Maharashtra, Karnataka, Andhra Pradesh, Madhya Pradesh, Orissa", "kharif", " Philippines, Taiwan, Portugal"],
    "soyabean":["/static/images2/soyabean.jpg",  "Madhya Pradesh, Maharashtra, Rajasthan, Madhya Pradesh and Maharashtra", "kharif", "Spain, Thailand, Singapore"],
    "urad":["/static/images2/urad.jpg",  "Andhra Pradesh, Maharashtra, Madhya Pradesh, Tamil Nadu", "rabi", "United States, Canada, United Arab Emirates"],
    "ragi":["/static/images2/ragi.jpg",  "Maharashtra, Tamil Nadu and Uttarakhand", "kharif", "United Arab Emirates, New Zealand, Bahrain"],
    "sunflower":["/static/images2/sunflower.jpg",  "Karnataka, Andhra Pradesh, Maharashtra, Bihar, Orissa", "rabi", "Phillippines, United States, Bangladesh"],
    "sugarcane":["/static/images2/sugarcane.jpg","Uttar Pradesh, Maharashtra, Tamil Nadu, Karnataka, Andhra Pradesh" , "kharif", "Kenya, United Arab Emirates, United Kingdom"]
    }
    return crop_data[crop_name]