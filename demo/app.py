import connexion
import prance
from flask_cors import CORS
from typing import Any, Dict
from pathlib import Path

def get_bundled_specs(main_file: Path) -> Dict[str, Any]:
    parser = prance.ResolvingParser(str(main_file.absolute()),
                                    lazy = True, strict = True)
    parser.parse()
    return parser.specification

app = connexion.App(__name__, specification_dir='swagger/')
CORS(app.app)

app.add_api(get_bundled_specs(Path('demo/swagger/api.yaml')), resolver = connexion.RestyResolver("cms_rest_api")) 


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
