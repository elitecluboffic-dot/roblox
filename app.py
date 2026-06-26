from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

COUNTRY_TO_LOCALE = {
    "ID": "id",
    "US": "en-us",
    "GB": "en-gb",
    "MY": "ms-my",
    "JP": "ja",
    "KR": "ko",
    "CN": "zh-cn",
    "TW": "zh-tw",
    "SG": "zh-sg",
    "TH": "th",
    "VN": "vi",
    "PH": "tl",
    "RU": "ru",
    "DE": "de-de",
    "FR": "fr-fr",
    "IT": "it",
    "ES": "es-es",
    "PT": "pt-pt",
    "BR": "pt-br",
    "AR": "es-ar",
    "MX": "es-mx",
    "SA": "ar",
    "TR": "tr",
    "IN": "hi",
    "PK": "ur",
    "BD": "bn",
    "UA": "uk",
    "PL": "pl",
    "NL": "nl",
    "SE": "sv",
    "NO": "nb",
    "FI": "fi",
    "DK": "da",
    "AU": "en-au",
    "CA": "en-ca",
    "NZ": "en-nz",
}

@app.route('/getflag', methods=['GET'])
def get_flag():
    ip = request.args.get('ip', '')
    if not ip:
        return jsonify({"locale": "default", "country": "unknown"})
    
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}?fields=countryCode,country", timeout=3)
        data = res.json()
        country_code = data.get("countryCode", "").upper()
        locale = COUNTRY_TO_LOCALE.get(country_code, "default")
        return jsonify({
            "locale": locale,
            "country": data.get("country", "unknown"),
            "code": country_code
        })
    except:
        return jsonify({"locale": "default", "country": "unknown"})

@app.route('/', methods=['GET'])
def index():
    return jsonify({"status": "Flag Backend Running!"})

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
