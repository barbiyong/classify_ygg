#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "ABICO", "growth": 15.200000000000003}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "AOT", "growth": 5.5096418732782375}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "FOCUS", "growth": 5.527638190954779}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "NEWS", "growth": 12.499999999999993}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "GL", "growth": 8.333333333333332}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "TAPAC", "growth": 10.454545454545459}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "BLISS", "growth": 10.454545454545459}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "SPPT", "growth": 18.70967741935484}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "BANPU", "growth": 8.474576271186441}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "ABC", "growth": 5.555555555555561}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "BRC", "growth": 5.555555555555561}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "BLAND", "growth": 6.211180124223594}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "BKKCP", "growth": 6.211180124223594}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "CPR", "growth": 11.85185185185185}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "TLUXE", "growth": 7.8125}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "KASET", "growth": 7.971014492753631}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "ACAP", "growth": 13.60544217687075}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "SGP", "growth": 6.422018348623847}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "CFRESH", "growth": 5.88235294117646}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "CPI", "growth": 6.796116504854374}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "EMC", "growth": 7.692307692307699}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "FMT", "growth": 5.343511450381679}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "GRAMMY", "growth": 10.465116279069772}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "FORTH", "growth": 5.38461538461538}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "IFEC", "growth": 5.676855895196502}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "INSURE", "growth": 5.676855895196502}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "PT", "growth": 7.407407407407398}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "UKEM", "growth": 6.140350877192988}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "DEMCO", "growth": 6.896551724137931}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "KCE", "growth": 5.579399141630901}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "DIMET", "growth": 23.008849557522126}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "MATI", "growth": 6.363636363636357}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "NPP", "growth": 7.1428571428571495}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "PICO", "growth": 8.900523560209432}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "PRO", "growth": 8.900523560209432}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "ROBINS", "growth": 5.761316872427984}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "ROH", "growth": 5.761316872427984}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "RS", "growth": 5.031446540880497}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "SFP", "growth": 18.27956989247312}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "SGF", "growth": 18.27956989247312}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "STA", "growth": 5.1282051282051215}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "BIG", "growth": 18.02575107296137}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "SKR", "growth": 6.091370558375635}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "TF", "growth": 6.382978723404255}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "VNT", "growth": 5.599999999999994}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "HTECH", "growth": 26.48648648648647}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "KAMART", "growth": 7.692307692307695}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "TCC-W2", "growth": 7.692307692307695}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "DIMET-W1", "growth": 10.000000000000009}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "DNA", "growth": 13.008130081300806}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "TH-W1", "growth": 12.50000000000001}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "CHO", "growth": 6.249999999999992}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "PTG", "growth": 5.217391304347826}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "NMG-W3", "growth": 9.523809523809533}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "BLAND-W4", "growth": 15.384615384615378}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "NINE-W1", "growth": 9.803921568627459}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "TVD-W1", "growth": 9.803921568627459}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "AUCT", "growth": 11.235955056179774}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "POLAR-W2", "growth": 11.235955056179774}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "M", "growth": 7.6190476190476195}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "FVC", "growth": 12.195121951219505}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "PRINC-W1", "growth": 12.195121951219505}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "MEGA", "growth": 13.333333333333334}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "CHO-W1", "growth": 13.333333333333334}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "OCEAN", "growth": 5.084745762711869}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "IFEC-W1", "growth": 8.108108108108103}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "LIT", "growth": 9.909909909909906}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "SAWAD", "growth": 8.280254777070063}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "TAPAC-W2", "growth": 13.989637305699478}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "PCA", "growth": 5.30303030303029}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "M-PAT", "growth": 5.30303030303029}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "SAPPE", "growth": 6.2015503875969}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "EIC-W1", "growth": 5.71428571428572}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "FSMART", "growth": 6.395348837209311}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "BRR", "growth": 6.349206349206354}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "PAE-W1", "growth": 6.349206349206354}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "MINT-W5", "growth": 9.183673469387763}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "CBG", "growth": 8.934707903780069}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "MTLS", "growth": 12.162162162162158}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "DNA-W1", "growth": 7.812499999999989}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "AJD-W1", "growth": 10.344827586206906}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "NDR", "growth": 6.956521739130442}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "NPP-W2", "growth": 5.172413793103453}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "UWC-W2", "growth": 9.999999999999995}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "TGPRO-W1", "growth": 19.99999999999999}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "FPI-W1", "growth": 9.859154929577475}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "TWZ-W4", "growth": 49.999999999999986}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "FVC-W1", "growth": 10.588235294117645}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "SIMAT-W3", "growth": 7.936507936507943}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "SAWAD-W1", "growth": 12.857142857142861}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "WIIK-W1", "growth": 7.964601769911512}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "TH-W2", "growth": 11.1111111111111}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "TPOLY-W2", "growth": 7.407407407407393}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "BR", "growth": 9.756097560975602}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "JMT-W1", "growth": 7.02702702702702}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "AEC-W4", "growth": 5.8823529411764595}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "COM7", "growth": 5.38461538461538}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "PIMO", "growth": 11.864406779661028}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "AIRA-W2", "growth": 10.52631578947368}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "T-W3", "growth": 16.666666666666682}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "NEWS-W5", "growth": 33.33333333333334}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "KOOL", "growth": 13.821138211382108}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "JWD", "growth": 5.3333333333333375}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "ORI", "growth": 74.69618055555554}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "TFG", "growth": 5.263157894736836}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "GUNKUL-W", "growth": 5.263157894736836}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "TNP", "growth": 12.307692307692301}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "TLHPF", "growth": 12.307692307692301}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "GTB", "growth": 5.2173913043478315}',
    '{"template_name": "stock growth more than 5 in 5 day", "stock_name": "ASN", "growth": 5.925925925925931}'
]


@app.route('/')
def get_tasks(): return jsonify({'tasks': tasks
                                 })


if __name__ == '__main__': app.run(debug=True)
