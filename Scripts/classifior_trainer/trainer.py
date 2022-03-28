#!/usr/bin/env python
# coding: utf-8

# Load data

# In[ ]:


import os
#dossier2='/media/cdong/Elements/these/Projet/Extractor/mots_embedded'
dossier2='/media/cdong/Elements/these/Projet/Extractor/mots_embedded'
event_sac=list()
for file in os.listdir(dossier2):
    with open(dossier2+"/"+file, "r", encoding="utf-8") as f:
        lf=f.read().split("\n\n\n\n")
        for part in lf:
            if len(part)>0:
                exec("event_sac.append("+part+")")
#the data are saved into a list "event_sac"


# registering the sac_de_mots of the first iteration, group 1

# In[ ]:


#group 1
tadmin = ["arrêta", "arrêtai", "arrêtaient", "arrêtais", "arrêtait", "arrêtant", "arrêtas", "arrêtasse", "arrêtassent", "arrêtasses", "arrêtassiez", "arrêtassions", "arrête", "arrêtent", "arrêter", "arrêtera", "arrêterai", "arrêteraient", "arrêterais", "arrêterait", "arrêteras", "arrêterez", "arrêteriez", "arrêterions", "arrêterons", "arrêteront", "arrêtes", "arrêtez", "arrêtiez", "arrêtions", "arrêtons", "arrêtâmes", "arrêtât", "arrêtâtes", "arrêtèrent", "arrêté", "arrêtée", "arrêtées", "arrêtés", "arrêt", "arrêts", "autorisa", "autorisai", "autorisaient", "autorisais", "autorisait", "autorisant", "autorisas", "autorisasse", "autorisassent", "autorisasses", "autorisassiez", "autorisassions", "autorise", "autorisent", "autoriser", "autorisera", "autoriserai", "autoriseraient", "autoriserais", "autoriserait", "autoriseras", "autoriserez", "autoriseriez", "autoriserions", "autoriserons", "autoriseront", "autorises", "autorisez", "autorisiez", "autorisions", "autorisons", "autorisâmes", "autorisât", "autorisâtes", "autorisèrent", "autorisé", "autorisée", "autorisées", "autorisés", "autorisation", "autorisations", "demanda", "demandai", "demandaient", "demandais", "demandait", "demandant", "demandas", "demandasse", "demandassent", "demandasses", "demandassiez", "demandassions", "demande", "demandent", "demander", "demandera", "demanderai", "demanderaient", "demanderais", "demanderait", "demanderas", "demanderez", "demanderiez", "demanderions", "demanderons", "demanderont", "demandes", "demandez", "demandiez", "demandions", "demandons", "demandâmes", "demandât", "demandâtes", "demandèrent", "demandé", "demandée", "demandées", "demandés", "demande", "demandes", "imposa", "imposai", "imposaient", "imposais", "imposait", "imposant", "imposas", "imposasse", "imposassent", "imposasses", "imposassiez", "imposassions", "impose", "imposent", "imposer", "imposera", "imposerai", "imposeraient", "imposerais", "imposerait", "imposeras", "imposerez", "imposeriez", "imposerions", "imposerons", "imposeront", "imposes", "imposez", "imposiez", "imposions", "imposons", "imposâmes", "imposât", "imposâtes", "imposèrent", "imposé", "imposée", "imposées", "imposés", "liquida", "liquidai", "liquidaient", "liquidais", "liquidait", "liquidant", "liquidas", "liquidasse", "liquidassent", "liquidasses", "liquidassiez", "liquidassions", "liquide", "liquident", "liquider", "liquidera", "liquiderai", "liquideraient", "liquiderais", "liquiderait", "liquideras", "liquiderez", "liquideriez", "liquiderions", "liquiderons", "liquideront", "liquides", "liquidez", "liquidiez", "liquidions", "liquidons", "liquidâmes", "liquidât", "liquidâtes", "liquidèrent", "liquidé", "liquidée", "liquidées", "liquidés", "liquidation", "liquidations", "prescrira", "prescrirai", "prescriraient", "prescrirais", "prescrirait", "prescriras", "prescrire", "prescrirez", "prescririez", "prescririons", "prescrirons", "prescriront", "prescris", "prescrit", "prescrite", "prescrites", "prescrits", "prescrivaient", "prescrivais", "prescrivait", "prescrivant", "prescrive", "prescrivent", "prescrives", "prescrivez", "prescriviez", "prescrivions", "prescrivirent", "prescrivis", "prescrivisse", "prescrivissent", "prescrivisses", "prescrivissiez", "prescrivissions", "prescrivit", "prescrivons", "prescrivîmes", "prescrivît", "prescrivîtes", "prescription", "prescriptions", "signa", "signai", "signaient", "signais", "signait", "signant", "signas", "signasse", "signassent", "signasses", "signassiez", "signassions", "signe", "signent", "signer", "signera", "signerai", "signeraient", "signerais", "signerait", "signeras", "signerez", "signeriez", "signerions", "signerons", "signeront", "signes", "signez", "signiez", "signions", "signons", "signâmes", "signât", "signâtes", "signèrent", "signé", "signée", "signées", "signés", "signature", "signatures", "transmet", "transmets", "transmettaient", "transmettais", "transmettait", "transmettant", "transmette", "transmettent", "transmettes", "transmettez", "transmettiez", "transmettions", "transmettons", "transmettra", "transmettrai", "transmettraient", "transmettrais", "transmettrait", "transmettras", "transmettre", "transmettrez", "transmettriez", "transmettrions", "transmettrons", "transmettront", "transmirent", "transmis", "transmise", "transmises", "transmisse", "transmissent", "transmisses", "transmissiez", "transmissions", "transmit", "transmîmes", "transmît", "transmîtes", "transmission", "transmissions", "rapporta", "rapportai", "rapportaient", "rapportais", "rapportait", "rapportant", "rapportas", "rapportasse", "rapportassent", "rapportasses", "rapportassiez", "rapportassions", "rapporte", "rapportent", "rapporter", "rapportera", "rapporterai", "rapporteraient", "rapporterais", "rapporterait", "rapporteras", "rapporterez", "rapporteriez", "rapporterions", "rapporterons", "rapporteront", "rapportes", "rapportez", "rapportiez", "rapportions", "rapportons", "rapportâmes", "rapportât", "rapportâtes", "rapportèrent", "rapporté", "rapportée", "rapportées", "rapportés", "rapport", "rapports"]
tdiag = ["analyse", "analyses", "analysa", "analysai", "analysaient", "analysais", "analysait", "analysant", "analysas", "analysasse", "analysassent", "analysasses", "analysassiez", "analysassions", "analyse", "analysent", "analyser", "analysera", "analyserai", "analyseraient", "analyserais", "analyserait", "analyseras", "analyserez", "analyseriez", "analyserions", "analyserons", "analyseront", "analyses", "analysez", "analysiez", "analysions", "analysons", "analysâmes", "analysât", "analysâtes", "analysèrent", "analysé", "analysée", "analysées", "analysés", "campagne", "campagnes", "diagnostiqua", "diagnostiquai", "diagnostiquaient", "diagnostiquais", "diagnostiquait", "diagnostiquant", "diagnostiquas", "diagnostiquasse", "diagnostiquassent", "diagnostiquasses", "diagnostiquassiez", "diagnostiquassions", "diagnostique", "diagnostiquent", "diagnostiquer", "diagnostiquera", "diagnostiquerai", "diagnostiqueraient", "diagnostiquerais", "diagnostiquerait", "diagnostiqueras", "diagnostiquerez", "diagnostiqueriez", "diagnostiquerions", "diagnostiquerons", "diagnostiqueront", "diagnostiques", "diagnostiquez", "diagnostiquiez", "diagnostiquions", "diagnostiquons", "diagnostiquâmes", "diagnostiquât", "diagnostiquâtes", "diagnostiquèrent", "diagnostiqué", "diagnostiquée", "diagnostiquées", "diagnostiqués", "diagnostic", "diagnostics", "établi", "établie", "établies", "établir", "établira", "établirai", "établiraient", "établirais", "établirait", "établiras", "établirent", "établirez", "établiriez", "établirions", "établirons", "établiront", "établis", "établissaient", "établissais", "établissait", "établissant", "établisse", "établissent", "établisses", "établissez", "établissiez", "établissions", "établissons", "établit", "établîmes", "établît", "établîtes", "étudia", "étudiai", "étudiaient", "étudiais", "étudiait", "étudiant", "étudias", "étudiasse", "étudiassent", "étudiasses", "étudiassiez", "étudiassions", "étudie", "étudient", "étudier", "étudiera", "étudierai", "étudieraient", "étudierais", "étudierait", "étudieras", "étudierez", "étudieriez", "étudierions", "étudierons", "étudieront", "étudies", "étudiez", "étudiiez", "étudiions", "étudions", "étudiâmes", "étudiât", "étudiâtes", "étudièrent", "étudié", "étudiée", "étudiées", "étudiés", "étude", "études", "inspecta", "inspectai", "inspectaient", "inspectais", "inspectait", "inspectant", "inspectas", "inspectasse", "inspectassent", "inspectasses", "inspectassiez", "inspectassions", "inspecte", "inspectent", "inspecter", "inspectera", "inspecterai", "inspecteraient", "inspecterais", "inspecterait", "inspecteras", "inspecterez", "inspecteriez", "inspecterions", "inspecterons", "inspecteront", "inspectes", "inspectez", "inspectiez", "inspections", "inspectons", "inspectâmes", "inspectât", "inspectâtes", "inspectèrent", "inspecté", "inspectée", "inspectées", "inspectés", "inspection", "inspections", "investigua", "investiguai", "investiguaient", "investiguais", "investiguait", "investiguant", "investiguas", "investiguasse", "investiguassent", "investiguasses", "investiguassiez", "investiguassions", "investigue", "investiguent", "investiguer", "investiguera", "investiguerai", "investigueraient", "investiguerais", "investiguerait", "investigueras", "investiguerez", "investigueriez", "investiguerions", "investiguerons", "investigueront", "investigues", "investiguez", "investiguiez", "investiguions", "investiguons", "investiguâmes", "investiguât", "investiguâtes", "investiguèrent", "investigué", "investiguée", "investiguées", "investigués", "investigation", "investigations", "mesura", "mesurai", "mesuraient", "mesurais", "mesurait", "mesurant", "mesuras", "mesurasse", "mesurassent", "mesurasses", "mesurassiez", "mesurassions", "mesure", "mesurent", "mesurer", "mesurera", "mesurerai", "mesureraient", "mesurerais", "mesurerait", "mesureras", "mesurerez", "mesureriez", "mesurerions", "mesurerons", "mesureront", "mesures", "mesurez", "mesuriez", "mesurions", "mesurons", "mesurâmes", "mesurât", "mesurâtes", "mesurèrent", "mesuré", "mesurée", "mesurées", "mesurés", "mesure", "mesures", "préleva", "prélevai", "prélevaient", "prélevais", "prélevait", "prélevant", "prélevas", "prélevasse", "prélevassent", "prélevasses", "prélevassiez", "prélevassions", "prélever", "prélevez", "préleviez", "prélevions", "prélevons", "prélevâmes", "prélevât", "prélevâtes", "prélevèrent", "prélevé", "prélevée", "prélevées", "prélevés", "prélève", "prélèvent", "prélèvera", "prélèverai", "prélèveraient", "prélèverais", "prélèverait", "prélèveras", "prélèverez", "prélèveriez", "prélèverions", "prélèverons", "prélèveront", "prélèves", "prélèvement", "prélèvements", "récola", "récolai", "récolaient", "récolais", "récolait", "récolant", "récolas", "récolasse", "récolassent", "récolasses", "récolassiez", "récolassions", "récole", "récolent", "récoler", "récolera", "récolerai", "récoleraient", "récolerais", "récolerait", "récoleras", "récolerez", "récoleriez", "récolerions", "récolerons", "récoleront", "récoles", "récolez", "récoliez", "récolions", "récolons", "récolâmes", "récolât", "récolâtes", "récolèrent", "récolé", "récolée", "récolées", "récolés", "récolement", "récolements", "remblaie", "remblaient", "remblaiera", "remblaierai", "remblaieraient", "remblaierais", "remblaierait", "remblaieras", "remblaierez", "remblaieriez", "remblaierions", "remblaierons", "remblaieront", "remblaies", "remblaya", "remblayai", "remblayaient", "remblayais", "remblayait", "remblayant", "remblayas", "remblayasse", "remblayassent", "remblayasses", "remblayassiez", "remblayassions", "remblaye", "remblayent", "remblayer", "remblayera", "remblayerai", "remblayeraient", "remblayerais", "remblayerait", "remblayeras", "remblayerez", "remblayeriez", "remblayerions", "remblayerons", "remblayeront", "remblayes", "remblayez", "remblayiez", "remblayions", "remblayons", "remblayâmes", "remblayât", "remblayâtes", "remblayèrent", "remblayé", "remblayée", "remblayées", "remblayés", "remblaiement", "remblaiements", "sonda", "sondai", "sondaient", "sondais", "sondait", "sondant", "sondas", "sondasse", "sondassent", "sondasses", "sondassiez", "sondassions", "sonde", "sondent", "sonder", "sondera", "sonderai", "sonderaient", "sonderais", "sonderait", "sonderas", "sonderez", "sonderiez", "sonderions", "sonderons", "sonderont", "sondes", "sondez", "sondiez", "sondions", "sondons", "sondâmes", "sondât", "sondâtes", "sondèrent", "sondé", "sondée", "sondées", "sondés", "sondage", "sondages", "surveilla", "surveillai", "surveillaient", "surveillais", "surveillait", "surveillant", "surveillas", "surveillasse", "surveillassent", "surveillasses", "surveillassiez", "surveillassions", "surveille", "surveillent", "surveiller", "surveillera", "surveillerai", "surveilleraient", "surveillerais", "surveillerait", "surveilleras", "surveillerez", "surveilleriez", "surveillerions", "surveillerons", "surveilleront", "surveilles", "surveillez", "surveilliez", "surveillions", "surveillons", "surveillâmes", "surveillât", "surveillâtes", "surveillèrent", "surveillé", "surveillée", "surveillées", "surveillés", "surveillance", "surveillances", "visita", "visitai", "visitaient", "visitais", "visitait", "visitant", "visitas", "visitasse", "visitassent", "visitasses", "visitassiez", "visitassions", "visite", "visitent", "visiter", "visitera", "visiterai", "visiteraient", "visiterais", "visiterait", "visiteras", "visiterez", "visiteriez", "visiterions", "visiterons", "visiteront", "visites", "visitez", "visitiez", "visitions", "visitons", "visitâmes", "visitât", "visitâtes", "visitèrent", "visité", "visitée", "visitées", "visités", "visite", "visites"]
tdepol = ["démantela", "démantelai", "démantelaient", "démantelais", "démantelait", "démantelant", "démantelas", "démantelasse", "démantelassent", "démantelasses", "démantelassiez", "démantelassions", "démanteler", "démantelez", "démanteliez", "démantelions", "démantelons", "démantelâmes", "démantelât", "démantelâtes", "démantelèrent", "démantelé", "démantelée", "démantelées", "démantelés", "démantèle", "démantèlent", "démantèlera", "démantèlerai", "démantèleraient", "démantèlerais", "démantèlerait", "démantèleras", "démantèlerez", "démantèleriez", "démantèlerions", "démantèlerons", "démantèleront", "démantèles", "démantèlement", "démantèlements", "dépollua", "dépolluai", "dépolluaient", "dépolluais", "dépolluait", "dépolluant", "dépolluas", "dépolluasse", "dépolluassent", "dépolluasses", "dépolluassiez", "dépolluassions", "dépollue", "dépolluent", "dépolluer", "dépolluera", "dépolluerai", "dépollueraient", "dépolluerais", "dépolluerait", "dépollueras", "dépolluerez", "dépollueriez", "dépolluerions", "dépolluerons", "dépollueront", "dépollues", "dépolluez", "dépolluiez", "dépolluions", "dépolluons", "dépolluâmes", "dépolluât", "dépolluâtes", "dépolluèrent", "dépollué", "dépolluée", "dépolluées", "dépollués", "dépollution", "dépollutions", "élimina", "éliminai", "éliminaient", "éliminais", "éliminait", "éliminant", "éliminas", "éliminasse", "éliminassent", "éliminasses", "éliminassiez", "éliminassions", "élimine", "éliminent", "éliminer", "éliminera", "éliminerai", "élimineraient", "éliminerais", "éliminerait", "élimineras", "éliminerez", "élimineriez", "éliminerions", "éliminerons", "élimineront", "élimines", "éliminez", "éliminiez", "éliminions", "éliminons", "éliminâmes", "éliminât", "éliminâtes", "éliminèrent", "éliminé", "éliminée", "éliminées", "éliminés", "élimination", "éliminations", "enleva", "enlevai", "enlevaient", "enlevais", "enlevait", "enlevant", "enlevas", "enlevasse", "enlevassent", "enlevasses", "enlevassiez", "enlevassions", "enlever", "enlevez", "enleviez", "enlevions", "enlevons", "enlevâmes", "enlevât", "enlevâtes", "enlevèrent", "enlevé", "enlevée", "enlevées", "enlevés", "enlève", "enlèvent", "enlèvera", "enlèverai", "enlèveraient", "enlèverais", "enlèverait", "enlèveras", "enlèverez", "enlèveriez", "enlèverions", "enlèverons", "enlèveront", "enlèves", "enlèvement", "enlèvements", "évacua", "évacuai", "évacuaient", "évacuais", "évacuait", "évacuant", "évacuas", "évacuasse", "évacuassent", "évacuasses", "évacuassiez", "évacuassions", "évacue", "évacuent", "évacuer", "évacuera", "évacuerai", "évacueraient", "évacuerais", "évacuerait", "évacueras", "évacuerez", "évacueriez", "évacuerions", "évacuerons", "évacueront", "évacues", "évacuez", "évacuiez", "évacuions", "évacuons", "évacuâmes", "évacuât", "évacuâtes", "évacuèrent", "évacué", "évacuée", "évacuées", "évacués", "évacuation", "évacuations", "excava", "excavai", "excavaient", "excavais", "excavait", "excavant", "excavas", "excavasse", "excavassent", "excavasses", "excavassiez", "excavassions", "excave", "excavent", "excaver", "excavera", "excaverai", "excaveraient", "excaverais", "excaverait", "excaveras", "excaverez", "excaveriez", "excaverions", "excaverons", "excaveront", "excaves", "excavez", "excaviez", "excavions", "excavons", "excavâmes", "excavât", "excavâtes", "excavèrent", "excavé", "excavée", "excavées", "excavés", "excavation", "excavations", "pompa", "pompai", "pompaient", "pompais", "pompait", "pompant", "pompas", "pompasse", "pompassent", "pompasses", "pompassiez", "pompassions", "pompe", "pompent", "pomper", "pompera", "pomperai", "pomperaient", "pomperais", "pomperait", "pomperas", "pomperez", "pomperiez", "pomperions", "pomperons", "pomperont", "pompes", "pompez", "pompiez", "pompions", "pompons", "pompâmes", "pompât", "pompâtes", "pompèrent", "pompé", "pompée", "pompées", "pompés", "pompage", "pompages", "réaménage", "réaménagea", "réaménageai", "réaménageaient", "réaménageais", "réaménageait", "réaménageant", "réaménageas", "réaménageasse", "réaménageassent", "réaménageasses", "réaménageassiez", "réaménageassions", "réaménagent", "réaménageons", "réaménager", "réaménagera", "réaménagerai", "réaménageraient", "réaménagerais", "réaménagerait", "réaménageras", "réaménagerez", "réaménageriez", "réaménagerions", "réaménagerons", "réaménageront", "réaménages", "réaménagez", "réaménageâmes", "réaménageât", "réaménageâtes", "réaménagiez", "réaménagions", "réaménagèrent", "réaménagé", "réaménagée", "réaménagées", "réaménagés", "réaménagement", "réaménagements", "réhabilita", "réhabilitai", "réhabilitaient", "réhabilitais", "réhabilitait", "réhabilitant", "réhabilitas", "réhabilitasse", "réhabilitassent", "réhabilitasses", "réhabilitassiez", "réhabilitassions", "réhabilite", "réhabilitent", "réhabiliter", "réhabilitera", "réhabiliterai", "réhabiliteraient", "réhabiliterais", "réhabiliterait", "réhabiliteras", "réhabiliterez", "réhabiliteriez", "réhabiliterions", "réhabiliterons", "réhabiliteront", "réhabilites", "réhabilitez", "réhabilitiez", "réhabilitions", "réhabilitons", "réhabilitâmes", "réhabilitât", "réhabilitâtes", "réhabilitèrent", "réhabilité", "réhabilitée", "réhabilitées", "réhabilités", "réhabilitation", "réhabilitations", "remise en état", "remises en état", "traita", "traitai", "traitaient", "traitais", "traitait", "traitant", "traitas", "traitasse", "traitassent", "traitasses", "traitassiez", "traitassions", "traite", "traitent", "traiter", "traitera", "traiterai", "traiteraient", "traiterais", "traiterait", "traiteras", "traiterez", "traiteriez", "traiterions", "traiterons", "traiteront", "traites", "traitez", "traitiez", "traitions", "traitons", "traitâmes", "traitât", "traitâtes", "traitèrent", "traité", "traitée", "traitées", "traités", "traitement", "traitements"]
tnuis = ["pollua", "polluai", "polluaient", "polluais", "polluait", "polluant", "polluas", "polluasse", "polluassent", "polluasses", "polluassiez", "polluassions", "pollue", "polluent", "polluer", "polluera", "polluerai", "pollueraient", "polluerais", "polluerait", "pollueras", "polluerez", "pollueriez", "polluerions", "polluerons", "pollueront", "pollues", "polluez", "polluiez", "polluions", "polluons", "polluâmes", "polluât", "polluâtes", "polluèrent", "pollué", "polluée", "polluées", "pollués", "pollution", "pollutions"]
tindus = ["accueillaient", "accueillais", "accueillait", "accueillant", "accueille", "accueillent", "accueillera", "accueillerai", "accueilleraient", "accueillerais", "accueillerait", "accueilleras", "accueillerez", "accueilleriez", "accueillerions", "accueillerons", "accueilleront", "accueilles", "accueillez", "accueilli", "accueillie", "accueillies", "accueilliez", "accueillions", "accueillir", "accueillirent", "accueillis", "accueillisse", "accueillissent", "accueillisses", "accueillissiez", "accueillissions", "accueillit", "accueillons", "accueillîmes", "accueillît", "accueillîtes", "accueil", "accueils", "activité", "activités", "aménage", "aménagea", "aménageai", "aménageaient", "aménageais", "aménageait", "aménageant", "aménageas", "aménageasse", "aménageassent", "aménageasses", "aménageassiez", "aménageassions", "aménagent", "aménageons", "aménager", "aménagera", "aménagerai", "aménageraient", "aménagerais", "aménagerait", "aménageras", "aménagerez", "aménageriez", "aménagerions", "aménagerons", "aménageront", "aménages", "aménagez", "aménageâmes", "aménageât", "aménageâtes", "aménagiez", "aménagions", "aménagèrent", "aménagé", "aménagée", "aménagées", "aménagés", "aménagement", "aménagements", "cessa", "cessai", "cessaient", "cessais", "cessait", "cessant", "cessas", "cessasse", "cessassent", "cessasses", "cessassiez", "cessassions", "cesse", "cessent", "cesser", "cessera", "cesserai", "cesseraient", "cesserais", "cesserait", "cesseras", "cesserez", "cesseriez", "cesserions", "cesserons", "cesseront", "cesses", "cessez", "cessiez", "cessions", "cessons", "cessâmes", "cessât", "cessâtes", "cessèrent", "cessé", "cessée", "cessées", "cessés", "construira", "construirai", "construiraient", "construirais", "construirait", "construiras", "construire", "construirez", "construiriez", "construirions", "construirons", "construiront", "construis", "construisaient", "construisais", "construisait", "construisant", "construise", "construisent", "construises", "construisez", "construisiez", "construisions", "construisirent", "construisis", "construisisse", "construisissent", "construisisses", "construisissiez", "construisissions", "construisit", "construisons", "construisîmes", "construisît", "construisîtes", "construit", "construite", "construites", "construits", "construction", "constructions", "déclara", "déclarai", "déclaraient", "déclarais", "déclarait", "déclarant", "déclaras", "déclarasse", "déclarassent", "déclarasses", "déclarassiez", "déclarassions", "déclare", "déclarent", "déclarer", "déclarera", "déclarerai", "déclareraient", "déclarerais", "déclarerait", "déclareras", "déclarerez", "déclareriez", "déclarerions", "déclarerons", "déclareront", "déclares", "déclarez", "déclariez", "déclarions", "déclarons", "déclarâmes", "déclarât", "déclarâtes", "déclarèrent", "déclaré", "déclarée", "déclarées", "déclarés", "déclaration", "déclarations", "démoli", "démolie", "démolies", "démolir", "démolira", "démolirai", "démoliraient", "démolirais", "démolirait", "démoliras", "démolirent", "démolirez", "démoliriez", "démolirions", "démolirons", "démoliront", "démolis", "démolissaient", "démolissais", "démolissait", "démolissant", "démolisse", "démolissent", "démolisses", "démolissez", "démolissiez", "démolissions", "démolissons", "démolit", "démolîmes", "démolît", "démolîtes", "démolition", "démolitions", "exploita", "exploitai", "exploitaient", "exploitais", "exploitait", "exploitant", "exploitas", "exploitasse", "exploitassent", "exploitasses", "exploitassiez", "exploitassions", "exploite", "exploitent", "exploiter", "exploitera", "exploiterai", "exploiteraient", "exploiterais", "exploiterait", "exploiteras", "exploiterez", "exploiteriez", "exploiterions", "exploiterons", "exploiteront", "exploites", "exploitez", "exploitiez", "exploitions", "exploitons", "exploitâmes", "exploitât", "exploitâtes", "exploitèrent", "exploité", "exploitée", "exploitées", "exploités", "exploitation", "exploitations", "implanta", "implantai", "implantaient", "implantais", "implantait", "implantant", "implantas", "implantasse", "implantassent", "implantasses", "implantassiez", "implantassions", "implante", "implantent", "implanter", "implantera", "implanterai", "implanteraient", "implanterais", "implanterait", "implanteras", "implanterez", "implanteriez", "implanterions", "implanterons", "implanteront", "implantes", "implantez", "implantiez", "implantions", "implantons", "implantâmes", "implantât", "implantâtes", "implantèrent", "implanté", "implantée", "implantées", "implantés", "implantation", "implantations", "installa", "installai", "installaient", "installais", "installait", "installant", "installas", "installasse", "installassent", "installasses", "installassiez", "installassions", "installe", "installent", "installer", "installera", "installerai", "installeraient", "installerais", "installerait", "installeras", "installerez", "installeriez", "installerions", "installerons", "installeront", "installes", "installez", "installiez", "installions", "installons", "installâmes", "installât", "installâtes", "installèrent", "installé", "installée", "installées", "installés", "projeta", "projetai", "projetaient", "projetais", "projetait", "projetant", "projetas", "projetasse", "projetassent", "projetasses", "projetassiez", "projetassions", "projeter", "projetez", "projetiez", "projetions", "projetons", "projette", "projettent", "projettera", "projetterai", "projetteraient", "projetterais", "projetterait", "projetteras", "projetterez", "projetteriez", "projetterions", "projetterons", "projetteront", "projettes", "projetâmes", "projetât", "projetâtes", "projetèrent", "projeté", "projetée", "projetées", "projetés", "projet", "projets", "usa", "usai", "usaient", "usais", "usait", "usant", "usas", "usasse", "usassent", "usasses", "usassiez", "usassions", "use", "usent", "user", "usera", "userai", "useraient", "userais", "userait", "useras", "userez", "useriez", "userions", "userons", "useront", "uses", "usez", "usiez", "usions", "usons", "usâmes", "usât", "usâtes", "usèrent", "usé", "usée", "usées", "usés", "usage", "usages", "vend", "vendaient", "vendais", "vendait", "vendant", "vende", "vendent", "vendes", "vendez", "vendiez", "vendions", "vendirent", "vendis", "vendisse", "vendissent", "vendisses", "vendissiez", "vendissions", "vendit", "vendons", "vendra", "vendrai", "vendraient", "vendrais", "vendrait", "vendras", "vendre", "vendrez", "vendriez", "vendrions", "vendrons", "vendront", "vends", "vendu", "vendue", "vendues", "vendus", "vendîmes", "vendît", "vendîtes", "vente", "ventes"]
tneutre = ["change", "changea", "changeai", "changeaient", "changeais", "changeait", "changeant", "changeas", "changeasse", "changeassent", "changeasses", "changeassiez", "changeassions", "changent", "changeons", "changer", "changera", "changerai", "changeraient", "changerais", "changerait", "changeras", "changerez", "changeriez", "changerions", "changerons", "changeront", "changes", "changez", "changeâmes", "changeât", "changeâtes", "changiez", "changions", "changèrent", "changé", "changée", "changées", "changés", "effectua", "effectuai", "effectuaient", "effectuais", "effectuait", "effectuant", "effectuas", "effectuasse", "effectuassent", "effectuasses", "effectuassiez", "effectuassions", "effectue", "effectuent", "effectuer", "effectuera", "effectuerai", "effectueraient", "effectuerais", "effectuerait", "effectueras", "effectuerez", "effectueriez", "effectuerions", "effectuerons", "effectueront", "effectues", "effectuez", "effectuiez", "effectuions", "effectuons", "effectuâmes", "effectuât", "effectuâtes", "effectuèrent", "effectué", "effectuée", "effectuées", "effectués", "installation", "installations", "mena", "menai", "menaient", "menais", "menait", "menant", "menas", "menasse", "menassent", "menasses", "menassiez", "menassions", "mener", "menez", "meniez", "menions", "menons", "menâmes", "menât", "menâtes", "menèrent", "mené", "menée", "menées", "menés", "mène", "mènent", "mènera", "mènerai", "mèneraient", "mènerais", "mènerait", "mèneras", "mènerez", "mèneriez", "mènerions", "mènerons", "mèneront", "mènes", "place", "places", "placement", "placements", "opère", "opèrent", "opères", "opéra", "opérai", "opéraient", "opérais", "opérait", "opérant", "opéras", "opérasse", "opérassent", "opérasses", "opérassiez", "opérassions", "opérer", "opérera", "opérerai", "opéreraient", "opérerais", "opérerait", "opéreras", "opérerez", "opéreriez", "opérerions", "opérerons", "opéreront", "opérez", "opériez", "opérions", "opérons", "opérâmes", "opérât", "opérâtes", "opérèrent", "opéré", "opérée", "opérées", "opérés", "opération", "opérations", "prenaient", "prenais", "prenait", "prenant", "prend", "prendra", "prendrai", "prendraient", "prendrais", "prendrait", "prendras", "prendre", "prendrez", "prendriez", "prendrions", "prendrons", "prendront", "prends", "prenez", "preniez", "prenions", "prenne", "prennent", "prennes", "prenons", "prirent", "pris", "prise", "prises", "prisse", "prissent", "prisses", "prissiez", "prissions", "prit", "prîmes", "prît", "prîtes", "prise", "prises", "réalisa", "réalisai", "réalisaient", "réalisais", "réalisait", "réalisant", "réalisas", "réalisasse", "réalisassent", "réalisasses", "réalisassiez", "réalisassions", "réalise", "réalisent", "réaliser", "réalisera", "réaliserai", "réaliseraient", "réaliserais", "réaliserait", "réaliseras", "réaliserez", "réaliseriez", "réaliserions", "réaliserons", "réaliseront", "réalises", "réalisez", "réalisiez", "réalisions", "réalisons", "réalisâmes", "réalisât", "réalisâtes", "réalisèrent", "réalisé", "réalisée", "réalisées", "réalisés", "réalisation", "réalisations", "remet", "remets", "remettaient", "remettais", "remettait", "remettant", "remette", "remettent", "remettes", "remettez", "remettiez", "remettions", "remettons", "remettra", "remettrai", "remettraient", "remettrais", "remettrait", "remettras", "remettre", "remettrez", "remettriez", "remettrions", "remettrons", "remettront", "remirent", "remis", "remise", "remises", "remisse", "remissent", "remisses", "remissiez", "remissions", "remit", "remîmes", "remît", "remîtes", "remise", "remises", "situa", "situai", "situaient", "situais", "situait", "situant", "situas", "situasse", "situassent", "situasses", "situassiez", "situassions", "situe", "situent", "situer", "situera", "situerai", "situeraient", "situerais", "situerait", "situeras", "situerez", "situeriez", "situerions", "situerons", "situeront", "situes", "situez", "situiez", "situions", "situons", "situâmes", "situât", "situâtes", "situèrent", "situé", "située", "situées", "situés", "situation", "situations"]


# registering the sac_de_mots of the second iteration, group 2

# In[ ]:


#group 2
fadmin = ['interdiction', 'interdictions', 'interdira', 'interdirai', 'interdiraient', 'interdirais', 'interdirait', 'interdiras', 'interdire', 'interdirent', 'interdirez', 'interdiriez', 'interdirions', 'interdirons', 'interdiront', 'interdis', 'interdisaient', 'interdisais', 'interdisait', 'interdisant', 'interdise', 'interdisent', 'interdises', 'interdisez', 'interdisiez', 'interdisions', 'interdisons', 'interdisse', 'interdissent', 'interdisses', 'interdissiez', 'interdissions', 'interdit', 'interdite', 'interdites', 'interdits', 'interdîmes', 'interdît', 'interdîtes', 'confinement', 'confinements', 'confina', 'confinai', 'confinaient', 'confinais', 'confinait', 'confinant', 'confinas', 'confinasse', 'confinassent', 'confinasses', 'confinassiez', 'confinassions', 'confine', 'confinent', 'confiner', 'confinera', 'confinerai', 'confineraient', 'confinerais', 'confinerait', 'confineras', 'confinerez', 'confineriez', 'confinerions', 'confinerons', 'confineront', 'confines', 'confinez', 'confiniez', 'confinions', 'confinons', 'confinâmes', 'confinât', 'confinâtes', 'confinèrent', 'confiné', 'confinée', 'confinées', 'confinés', 'demeure', 'demeures',
'constata', 'constatai', 'constataient', 'constatais', 'constatait', 'constatant', 'constatas', 'constatasse', 'constatassent', 'constatasses', 'constatassiez', 'constatassions', 'constate', 'constatent', 'constater', 'constatera', 'constaterai', 'constateraient', 'constaterais', 'constaterait', 'constateras', 'constaterez', 'constateriez', 'constaterions', 'constaterons', 'constateront', 'constates', 'constatez', 'constatiez', 'constations', 'constatons', 'constatâmes', 'constatât', 'constatâtes', 'constatèrent', 'constaté', 'constatée', 'constatées', 'constatés', 'constat', 'constats', 'contrôla', 'contrôlai', 'contrôlaient', 'contrôlais', 'contrôlait', 'contrôlant', 'contrôlas', 'contrôlasse', 'contrôlassent', 'contrôlasses', 'contrôlassiez', 'contrôlassions', 'contrôle', 'contrôlent', 'contrôler', 'contrôlera', 'contrôlerai', 'contrôleraient', 'contrôlerais', 'contrôlerait', 'contrôleras', 'contrôlerez', 'contrôleriez', 'contrôlerions', 'contrôlerons', 'contrôleront', 'contrôles', 'contrôlez', 'contrôliez', 'contrôlions', 'contrôlons', 'contrôlâmes', 'contrôlât', 'contrôlâtes', 'contrôlèrent', 'contrôlé', 'contrôlée', 'contrôlées', 'contrôlés', 'contrôle', 'contrôles', 'réunion', 'réunions',]
fdiag = ['découverte', 'découvertes', 'découvert', 'découverte', 'découvertes', 'découverts', 'découvraient', 'découvrais', 'découvrait', 'découvrant', 'découvre', 'découvrent', 'découvres', 'découvrez', 'découvriez', 'découvrions', 'découvrir', 'découvrira', 'découvrirai', 'découvriraient', 'découvrirais', 'découvrirait', 'découvriras', 'découvrirent', 'découvrirez', 'découvririez', 'découvririons', 'découvrirons', 'découvriront', 'découvris', 'découvrisse', 'découvrissent', 'découvrisses', 'découvrissiez', 'découvrissions', 'découvrit', 'découvrons', 'découvrîmes', 'découvrît', 'découvrîtes', 'détecta', 'détectai', 'détectaient', 'détectais', 'détectait', 'détectant', 'détectas', 'détectasse', 'détectassent', 'détectasses', 'détectassiez', 'détectassions', 'détecte', 'détectent', 'détecter', 'détectera', 'détecterai', 'détecteraient', 'détecterais', 'détecterait', 'détecteras', 'détecterez', 'détecteriez', 'détecterions', 'détecterons', 'détecteront', 'détectes', 'détectez', 'détectiez', 'détections', 'détectons', 'détectâmes', 'détectât', 'détectâtes', 'détectèrent', 'détecté', 'détectée', 'détectées', 'détectés', 'détection', 'détections', 'identifia', 'identifiai', 'identifiaient', 'identifiais', 'identifiait', 'identifiant', 'identifias', 'identifiasse', 'identifiassent', 'identifiasses', 'identifiassiez', 'identifiassions', 'identifie', 'identifient', 'identifier', 'identifiera', 'identifierai', 'identifieraient', 'identifierais', 'identifierait', 'identifieras', 'identifierez', 'identifieriez', 'identifierions', 'identifierons', 'identifieront', 'identifies', 'identifiez', 'identifiiez', 'identifiions', 'identifions', 'identifiâmes', 'identifiât', 'identifiâtes', 'identifièrent', 'identifié', 'identifiée', 'identifiées', 'identifiés', 'identification', 'identifications']
fdepol = ['comblement', 'comblements', 'combla', 'comblai', 'comblaient', 'comblais', 'comblait', 'comblant', 'comblas', 'comblasse', 'comblassent', 'comblasses', 'comblassiez', 'comblassions', 'comble', 'comblent', 'combler', 'comblera', 'comblerai', 'combleraient', 'comblerais', 'comblerait', 'combleras', 'comblerez', 'combleriez', 'comblerions', 'comblerons', 'combleront', 'combles', 'comblez', 'combliez', 'comblions', 'comblons', 'comblâmes', 'comblât', 'comblâtes', 'comblèrent', 'comblé', 'comblée', 'comblées', 'comblés', 'curage', 'curages', 'cura', 'curai', 'curaient', 'curais', 'curait', 'curant', 'curas', 'curasse', 'curassent', 'curasses', 'curassiez', 'curassions', 'cure', 'curent', 'curer', 'curera', 'curerai', 'cureraient', 'curerais', 'curerait', 'cureras', 'curerez', 'cureriez', 'curerions', 'curerons', 'cureront', 'cures', 'curez', 'curiez', 'curions', 'curons', 'curâmes', 'curât', 'curâtes', 'curèrent', 'curé', 'curée', 'curées', 'curés', 'dégazage', 'dégazages', 'dégaza', 'dégazai', 'dégazaient', 'dégazais', 'dégazait', 'dégazant', 'dégazas', 'dégazasse', 'dégazassent', 'dégazasses', 'dégazassiez', 'dégazassions', 'dégaze', 'dégazent', 'dégazer', 'dégazera', 'dégazerai', 'dégazeraient', 'dégazerais', 'dégazerait', 'dégazeras', 'dégazerez', 'dégazeriez', 'dégazerions', 'dégazerons', 'dégazeront', 'dégazes', 'dégazez', 'dégaziez', 'dégazions', 'dégazons', 'dégazâmes', 'dégazât', 'dégazâtes', 'dégazèrent', 'dégazé', 'dégazée', 'dégazées', 'dégazés', 'extraction', 'extractions', 'extraie', 'extraient', 'extraies', 'extraira', 'extrairai', 'extrairaient', 'extrairais', 'extrairait', 'extrairas', 'extraire', 'extrairez', 'extrairiez', 'extrairions', 'extrairons', 'extrairont', 'extrais', 'extrait', 'extraite', 'extraites', 'extraits', 'extrayaient', 'extrayais', 'extrayait', 'extrayant', 'extrayez', 'extrayiez', 'extrayions', 'extrayons', 'nettoyage', 'nettoyages', 'nettoie', 'nettoient', 'nettoiera', 'nettoierai', 'nettoieraient', 'nettoierais', 'nettoierait', 'nettoieras', 'nettoierez', 'nettoieriez', 'nettoierions', 'nettoierons', 'nettoieront', 'nettoies', 'nettoya', 'nettoyai', 'nettoyaient', 'nettoyais', 'nettoyait', 'nettoyant', 'nettoyas', 'nettoyasse', 'nettoyassent', 'nettoyasses', 'nettoyassiez', 'nettoyassions', 'nettoyer', 'nettoyez', 'nettoyiez', 'nettoyions', 'nettoyons', 'nettoyâmes', 'nettoyât', 'nettoyâtes', 'nettoyèrent', 'nettoyé', 'nettoyée', 'nettoyées', 'nettoyés', 'neutralisation', 'neutralisations', 'neutralisa', 'neutralisai', 'neutralisaient', 'neutralisais', 'neutralisait', 'neutralisant', 'neutralisas', 'neutralisasse', 'neutralisassent', 'neutralisasses', 'neutralisassiez', 'neutralisassions', 'neutralise', 'neutralisent', 'neutraliser', 'neutralisera', 'neutraliserai', 'neutraliseraient', 'neutraliserais', 'neutraliserait', 'neutraliseras', 'neutraliserez', 'neutraliseriez', 'neutraliserions', 'neutraliserons', 'neutraliseront', 'neutralises', 'neutralisez', 'neutralisiez', 'neutralisions', 'neutralisons', 'neutralisâmes', 'neutralisât', 'neutralisâtes', 'neutralisèrent', 'neutralisé', 'neutralisée', 'neutralisées', 'neutralisés', 'terrassement', 'terrassements', 'terrassa', 'terrassai', 'terrassaient', 'terrassais', 'terrassait', 'terrassant', 'terrassas', 'terrassasse', 'terrassassent', 'terrassasses', 'terrassassiez', 'terrassassions', 'terrasse', 'terrassent', 'terrasser', 'terrassera', 'terrasserai', 'terrasseraient', 'terrasserais', 'terrasserait', 'terrasseras', 'terrasserez', 'terrasseriez', 'terrasserions', 'terrasserons', 'terrasseront', 'terrasses', 'terrassez', 'terrassiez', 'terrassions', 'terrassons', 'terrassâmes', 'terrassât', 'terrassâtes', 'terrassèrent', 'terrassé', 'terrassée', 'terrassées', 'terrassés', 'vidange', 'vidanges', 'vidange', 'vidangea', 'vidangeai', 'vidangeaient', 'vidangeais', 'vidangeait', 'vidangeant', 'vidangeas', 'vidangeasse', 'vidangeassent', 'vidangeasses', 'vidangeassiez', 'vidangeassions', 'vidangent', 'vidangeons', 'vidanger', 'vidangera', 'vidangerai', 'vidangeraient', 'vidangerais', 'vidangerait', 'vidangeras', 'vidangerez', 'vidangeriez', 'vidangerions', 'vidangerons', 'vidangeront', 'vidanges', 'vidangez', 'vidangeâmes', 'vidangeât', 'vidangeâtes', 'vidangiez', 'vidangions', 'vidangèrent', 'vidangé', 'vidangée', 'vidangées', 'vidangés', ]
fnuis = ['déversement', 'déversements', 'déversa', 'déversai', 'déversaient', 'déversais', 'déversait', 'déversant', 'déversas', 'déversasse', 'déversassent', 'déversasses', 'déversassiez', 'déversassions', 'déverse', 'déversent', 'déverser', 'déversera', 'déverserai', 'déverseraient', 'déverserais', 'déverserait', 'déverseras', 'déverserez', 'déverseriez', 'déverserions', 'déverserons', 'déverseront', 'déverses', 'déversez', 'déversiez', 'déversions', 'déversons', 'déversâmes', 'déversât', 'déversâtes', 'déversèrent', 'déversé', 'déversée', 'déversées', 'déversés', 'fuite', 'fuites', 'fui', 'fuie', 'fuient', 'fuies', 'fuir', 'fuira', 'fuirai', 'fuiraient', 'fuirais', 'fuirait', 'fuiras', 'fuirent', 'fuirez', 'fuiriez', 'fuirions', 'fuirons', 'fuiront', 'fuis', 'fuisse', 'fuissent', 'fuisses', 'fuissiez', 'fuissions', 'fuit', 'fuyaient', 'fuyais', 'fuyait', 'fuyant', 'fuyez', 'fuyiez', 'fuyions', 'fuyons', 'fuîmes', 'fuît', 'fuîtes', 'incendie', 'incendies', 'incendia', 'incendiai', 'incendiaient', 'incendiais', 'incendiait', 'incendiant', 'incendias', 'incendiasse', 'incendiassent', 'incendiasses', 'incendiassiez', 'incendiassions', 'incendie', 'incendient', 'incendier', 'incendiera', 'incendierai', 'incendieraient', 'incendierais', 'incendierait', 'incendieras', 'incendierez', 'incendieriez', 'incendierions', 'incendierons', 'incendieront', 'incendies', 'incendiez', 'incendiiez', 'incendiions', 'incendions', 'incendiâmes', 'incendiât', 'incendiâtes', 'incendièrent', 'incendié', 'incendiée', 'incendiées', 'incendiés',]
findus = ['racheta', 'rachetai', 'rachetaient', 'rachetais', 'rachetait', 'rachetant', 'rachetas', 'rachetasse', 'rachetassent', 'rachetasses', 'rachetassiez', 'rachetassions', 'rachete', 'rachetent', 'racheter', 'rachetera', 'racheterai', 'racheteraient', 'racheterais', 'racheterait', 'racheteras', 'racheterez', 'racheteriez', 'racheterions', 'racheterons', 'racheteront', 'rachetes', 'rachetez', 'rachetiez', 'rachetions', 'rachetons', 'rachetâmes', 'rachetât', 'rachetâtes', 'rachetèrent', 'racheté', 'rachetée', 'rachetées', 'rachetés', 'rachète', 'rachètent', 'rachètera', 'rachèterai', 'rachèteraient', 'rachèterais', 'rachèterait', 'rachèteras', 'rachèterez', 'rachèteriez', 'rachèterions', 'rachèterons', 'rachèteront', 'rachètes', 'rachat', 'rachats',]
fneutre = ['travaux', 'complète', 'complètent', 'complètes', 'compléta', 'complétai', 'complétaient', 'complétais', 'complétait', 'complétant', 'complétas', 'complétasse', 'complétassent', 'complétasses', 'complétassiez', 'complétassions', 'compléter', 'complétera', 'compléterai', 'compléteraient', 'compléterais', 'compléterait', 'compléteras', 'compléterez', 'compléteriez', 'compléterions', 'compléterons', 'compléteront', 'complétez', 'complétiez', 'complétions', 'complétons', 'complétâmes', 'complétât', 'complétâtes', 'complétèrent', 'complété', 'complétée', 'complétées', 'complétés', 'examen', 'examens', 'examina', 'examinai', 'examinaient', 'examinais', 'examinait', 'examinant', 'examinas', 'examinasse', 'examinassent', 'examinasses', 'examinassiez', 'examinassions', 'examine', 'examinent', 'examiner', 'examinera', 'examinerai', 'examineraient', 'examinerais', 'examinerait', 'examineras', 'examinerez', 'examineriez', 'examinerions', 'examinerons', 'examineront', 'examines', 'examinez', 'examiniez', 'examinions', 'examinons', 'examinâmes', 'examinât', 'examinâtes', 'examinèrent', 'examiné', 'examinée', 'examinées', 'examinés', 'informa', 'informai', 'informaient', 'informais', 'informait', 'informant', 'informas', 'informasse', 'informassent', 'informasses', 'informassiez', 'informassions', 'informe', 'informent', 'informer', 'informera', 'informerai', 'informeraient', 'informerais', 'informerait', 'informeras', 'informerez', 'informeriez', 'informerions', 'informerons', 'informeront', 'informes', 'informez', 'informiez', 'informions', 'informons', 'informâmes', 'informât', 'informâtes', 'informèrent', 'informé', 'informée', 'informées', 'informés', 'information', 'informations', 'intervenaient', 'intervenais', 'intervenait', 'intervenant', 'intervenez', 'interveniez', 'intervenions', 'intervenir', 'intervenons', 'intervenu', 'intervenue', 'intervenues', 'intervenus', 'interviendra', 'interviendrai', 'interviendraient', 'interviendrais', 'interviendrait', 'interviendras', 'interviendrez', 'interviendriez', 'interviendrions', 'interviendrons', 'interviendront', 'intervienne', 'interviennent', 'interviennes', 'interviens', 'intervient', 'intervinrent', 'intervins', 'intervinsse', 'intervinssent', 'intervinsses', 'intervinssiez', 'intervinssions', 'intervint', 'intervînmes', 'intervînt', 'intervîntes', 'intervention', 'interventions', 'déposa', 'déposai', 'déposaient', 'déposais', 'déposait', 'déposant', 'déposas', 'déposasse', 'déposassent', 'déposasses', 'déposassiez', 'déposassions', 'dépose', 'déposent', 'déposer', 'déposera', 'déposerai', 'déposeraient', 'déposerais', 'déposerait', 'déposeras', 'déposerez', 'déposeriez', 'déposerions', 'déposerons', 'déposeront', 'déposes', 'déposez', 'déposiez', 'déposions', 'déposons', 'déposâmes', 'déposât', 'déposâtes', 'déposèrent', 'déposé', 'déposée', 'déposées', 'déposés', 'constata', 'constatai', 'constataient', 'constatais', 'constatait', 'constatant', 'constatas', 'constatasse', 'constatassent', 'constatasses', 'constatassiez', 'constatassions', 'constate', 'constatent', 'constater', 'constatera', 'constaterai', 'constateraient', 'constaterais', 'constaterait', 'constateras', 'constaterez', 'constateriez', 'constaterions', 'constaterons', 'constateront', 'constates', 'constatez', 'constatiez', 'constations', 'constatons', 'constatâmes', 'constatât', 'constatâtes', 'constatèrent', 'constaté', 'constatée', 'constatées', 'constatés', 'constat', 'constats', 'procède', 'procèdent', 'procèdes', 'procéda', 'procédai', 'procédaient', 'procédais', 'procédait', 'procédant', 'procédas', 'procédasse', 'procédassent', 'procédasses', 'procédassiez', 'procédassions', 'procéder', 'procédera', 'procéderai', 'procéderaient', 'procéderais', 'procéderait', 'procéderas', 'procéderez', 'procéderiez', 'procéderions', 'procéderons', 'procéderont', 'procédez', 'procédiez', 'procédions', 'procédons', 'procédâmes', 'procédât', 'procédâtes', 'procédèrent', 'procédé', 'recevaient', 'recevais', 'recevait', 'recevant', 'recevez', 'receviez', 'recevions', 'recevoir', 'recevons', 'recevra', 'recevrai', 'recevraient', 'recevrais', 'recevrait', 'recevras', 'recevrez', 'recevriez', 'recevrions', 'recevrons', 'recevront', 'reçois', 'reçoit', 'reçoive', 'reçoivent', 'reçoives', 'reçu', 'reçue', 'reçues', 'reçurent', 'reçus', 'reçusse', 'reçussent', 'reçusses', 'reçussiez', 'reçussions', 'reçut', 'reçûmes', 'reçût', 'reçûtes', 'réception', 'réceptions',]


# In[ ]:


#a fonction to join groups
def join_lists(a,b):
    c=set()
    for e in a:
        c.add(e)
    for f in b:
        c.add(f)
    return list(c)


# the first model is trained on group 1 and evaluated on group 2

# the second model is trained on group 1+2 and evaluated on group 3

# the following operation is to combine group 1 and group 2 to form group 1+2

# In[ ]:


#group 1+2
tadmin=join_lists(tadmin,fadmin)
tdiag=join_lists(tdiag,fdiag)
tdepol=join_lists(tdepol,fdepol)
tnuis=join_lists(tnuis,fnuis)
tindus=join_lists(tindus,findus)
tneutre=join_lists(tneutre,fneutre)


# registering the sac_de_mots of the third iteration, group 3

# In[ ]:


#group 3
fadmin = ['notification', 'notifications', 'notifia', 'notifiai', 'notifiaient', 'notifiais', 'notifiait', 'notifiant', 'notifias', 'notifiasse', 'notifiassent', 'notifiasses', 'notifiassiez', 'notifiassions', 'notifie', 'notifient', 'notifier', 'notifiera', 'notifierai', 'notifieraient', 'notifierais', 'notifierait', 'notifieras', 'notifierez', 'notifieriez', 'notifierions', 'notifierons', 'notifieront', 'notifies', 'notifiez', 'notifiiez', 'notifiions', 'notifions', 'notifiâmes', 'notifiât', 'notifiâtes', 'notifièrent', 'notifié', 'notifiée', 'notifiées', 'notifiés', 'acta', 'actai', 'actaient', 'actais', 'actait', 'actant', 'actas', 'actasse', 'actassent', 'actasses', 'actassiez', 'actassions', 'acte', 'actent', 'acter', 'actera', 'acterai', 'acteraient', 'acterais', 'acterait', 'acteras', 'acterez', 'acteriez', 'acterions', 'acterons', 'acteront', 'actes', 'actez', 'actiez', 'actions', 'actons', 'actâmes', 'actât', 'actâtes', 'actèrent', 'acté', 'actée', 'actées', 'actés', 'rédige', 'rédigea', 'rédigeai', 'rédigeaient', 'rédigeais', 'rédigeait', 'rédigeant', 'rédigeas', 'rédigeasse', 'rédigeassent', 'rédigeasses', 'rédigeassiez', 'rédigeassions', 'rédigent', 'rédigeons', 'rédiger', 'rédigera', 'rédigerai', 'rédigeraient', 'rédigerais', 'rédigerait', 'rédigeras', 'rédigerez', 'rédigeriez', 'rédigerions', 'rédigerons', 'rédigeront', 'rédiges', 'rédigez', 'rédigeâmes', 'rédigeât', 'rédigeâtes', 'rédigiez', 'rédigions', 'rédigèrent', 'rédigé', 'rédigée', 'rédigées', 'rédigés', 'mandata', 'mandatai', 'mandataient', 'mandatais', 'mandatait', 'mandatant', 'mandatas', 'mandatasse', 'mandatassent', 'mandatasses', 'mandatassiez', 'mandatassions', 'mandate', 'mandatent', 'mandater', 'mandatera', 'mandaterai', 'mandateraient', 'mandaterais', 'mandaterait', 'mandateras', 'mandaterez', 'mandateriez', 'mandaterions', 'mandaterons', 'mandateront', 'mandates', 'mandatez', 'mandatiez', 'mandations', 'mandatons', 'mandatâmes', 'mandatât', 'mandatâtes', 'mandatèrent', 'mandaté', 'mandatée', 'mandatées', 'mandatés', 'gestion', 'gestions', 'bilan', 'bilans', ]
fdiag = ['évaluation', 'évaluations', 'évalua', 'évaluai', 'évaluaient', 'évaluais', 'évaluait', 'évaluant', 'évaluas', 'évaluasse', 'évaluassent', 'évaluasses', 'évaluassiez', 'évaluassions', 'évalue', 'évaluent', 'évaluer', 'évaluera', 'évaluerai', 'évalueraient', 'évaluerais', 'évaluerait', 'évalueras', 'évaluerez', 'évalueriez', 'évaluerions', 'évaluerons', 'évalueront', 'évalues', 'évaluez', 'évaluiez', 'évaluions', 'évaluons', 'évaluâmes', 'évaluât', 'évaluâtes', 'évaluèrent', 'évalué', 'évaluée', 'évaluées', 'évalués', 'évidence', 'évidences', 'requalifia', 'requalifiai', 'requalifiaient', 'requalifiais', 'requalifiait', 'requalifiant', 'requalifias', 'requalifiasse', 'requalifiassent', 'requalifiasses', 'requalifiassiez', 'requalifiassions', 'requalifie', 'requalifient', 'requalifier', 'requalifiera', 'requalifierai', 'requalifieraient', 'requalifierais', 'requalifierait', 'requalifieras', 'requalifierez', 'requalifieriez', 'requalifierions', 'requalifierons', 'requalifieront', 'requalifies', 'requalifiez', 'requalifiiez', 'requalifiions', 'requalifions', 'requalifiâmes', 'requalifiât', 'requalifiâtes', 'requalifièrent', 'requalifié', 'requalifiée', 'requalifiées', 'requalifiés', 'requalification', 'requalifications', ]
fdepol = ['écrème', 'écrèment', 'écrèmes', 'écréma', 'écrémai', 'écrémaient', 'écrémais', 'écrémait', 'écrémant', 'écrémas', 'écrémasse', 'écrémassent', 'écrémasses', 'écrémassiez', 'écrémassions', 'écrémer', 'écrémera', 'écrémerai', 'écrémeraient', 'écrémerais', 'écrémerait', 'écrémeras', 'écrémerez', 'écrémeriez', 'écrémerions', 'écrémerons', 'écrémeront', 'écrémez', 'écrémiez', 'écrémions', 'écrémons', 'écrémâmes', 'écrémât', 'écrémâtes', 'écrémèrent', 'écrémé', 'écrémée', 'écrémées', 'écrémés', 'imperméabilisation', 'imperméabilisations', 'pose', 'poses', 'décapage', 'décapages', 'requalification', 'requalifications', 'incinération', 'incinérations', 'incinère', 'incinèrent', 'incinères', 'incinéra', 'incinérai', 'incinéraient', 'incinérais', 'incinérait', 'incinérant', 'incinéras', 'incinérasse', 'incinérassent', 'incinérasses', 'incinérassiez', 'incinérassions', 'incinérer', 'incinérera', 'incinérerai', 'incinéreraient', 'incinérerais', 'incinérerait', 'incinéreras', 'incinérerez', 'incinéreriez', 'incinérerions', 'incinérerons', 'incinéreront', 'incinérez', 'incinériez', 'incinérions', 'incinérons', 'incinérâmes', 'incinérât', 'incinérâtes', 'incinérèrent', 'incinéré', 'incinérée', 'incinérées', 'incinérés', 'suppression', 'suppressions', 'supprima', 'supprimai', 'supprimaient', 'supprimais', 'supprimait', 'supprimant', 'supprimas', 'supprimasse', 'supprimassent', 'supprimasses', 'supprimassiez', 'supprimassions', 'supprime', 'suppriment', 'supprimer', 'supprimera', 'supprimerai', 'supprimeraient', 'supprimerais', 'supprimerait', 'supprimeras', 'supprimerez', 'supprimeriez', 'supprimerions', 'supprimerons', 'supprimeront', 'supprimes', 'supprimez', 'supprimiez', 'supprimions', 'supprimons', 'supprimâmes', 'supprimât', 'supprimâtes', 'supprimèrent', 'supprimé', 'supprimée', 'supprimées', 'supprimés', 'sécurité', 'sécurités', ]
fnuis= ['impact', 'impacts', 'impacta', 'impactai', 'impactaient', 'impactais', 'impactait', 'impactant', 'impactas', 'impactasse', 'impactassent', 'impactasses', 'impactassiez', 'impactassions', 'impacte', 'impactent', 'impacter', 'impactera', 'impacterai', 'impacteraient', 'impacterais', 'impacterait', 'impacteras', 'impacterez', 'impacteriez', 'impacterions', 'impacterons', 'impacteront', 'impactes', 'impactez', 'impactiez', 'impactions', 'impactons', 'impactâmes', 'impactât', 'impactâtes', 'impactèrent', 'impacté', 'impactée', 'impactées', 'impactés', 'contamination', 'contaminations', 'contamina', 'contaminai', 'contaminaient', 'contaminais', 'contaminait', 'contaminant', 'contaminas', 'contaminasse', 'contaminassent', 'contaminasses', 'contaminassiez', 'contaminassions', 'contamine', 'contaminent', 'contaminer', 'contaminera', 'contaminerai', 'contamineraient', 'contaminerais', 'contaminerait', 'contamineras', 'contaminerez', 'contamineriez', 'contaminerions', 'contaminerons', 'contamineront', 'contamines', 'contaminez', 'contaminiez', 'contaminions', 'contaminons', 'contaminâmes', 'contaminât', 'contaminâtes', 'contaminèrent', 'contaminé', 'contaminée', 'contaminées', 'contaminés', 'émission', 'émissions', ]
findus = ['fermeture', 'fermetures', 'acquisition', 'acquisitions', 'acquerra', 'acquerrai', 'acquerraient', 'acquerrais', 'acquerrait', 'acquerras', 'acquerrez', 'acquerriez', 'acquerrions', 'acquerrons', 'acquerront', 'acquiers', 'acquiert', 'acquirent', 'acquis', 'acquise', 'acquises', 'acquisse', 'acquissent', 'acquisses', 'acquissiez', 'acquissions', 'acquit', 'acquière', 'acquièrent', 'acquières', 'acquéraient', 'acquérais', 'acquérait', 'acquérant', 'acquérez', 'acquériez', 'acquérions', 'acquérir', 'acquérons', 'acquîmes', 'acquît', 'acquîtes', 'hiérarchisa', 'hiérarchisai', 'hiérarchisaient', 'hiérarchisais', 'hiérarchisait', 'hiérarchisant', 'hiérarchisas', 'hiérarchisasse', 'hiérarchisassent', 'hiérarchisasses', 'hiérarchisassiez', 'hiérarchisassions', 'hiérarchise', 'hiérarchisent', 'hiérarchiser', 'hiérarchisera', 'hiérarchiserai', 'hiérarchiseraient', 'hiérarchiserais', 'hiérarchiserait', 'hiérarchiseras', 'hiérarchiserez', 'hiérarchiseriez', 'hiérarchiserions', 'hiérarchiserons', 'hiérarchiseront', 'hiérarchises', 'hiérarchisez', 'hiérarchisiez', 'hiérarchisions', 'hiérarchisons', 'hiérarchisâmes', 'hiérarchisât', 'hiérarchisâtes', 'hiérarchisèrent', 'hiérarchisé', 'hiérarchisée', 'hiérarchisées', 'hiérarchisés', 'propriétaire', 'propriétaires', 'exerce', 'exercent', 'exercer', 'exercera', 'exercerai', 'exerceraient', 'exercerais', 'exercerait', 'exerceras', 'exercerez', 'exerceriez', 'exercerions', 'exercerons', 'exerceront', 'exerces', 'exercez', 'exerciez', 'exercions', 'exercèrent', 'exercé', 'exercée', 'exercées', 'exercés', 'exerça', 'exerçai', 'exerçaient', 'exerçais', 'exerçait', 'exerçant', 'exerças', 'exerçasse', 'exerçassent', 'exerçasses', 'exerçassiez', 'exerçassions', 'exerçons', 'exerçâmes', 'exerçât', 'exerçâtes', 'occupa', 'occupai', 'occupaient', 'occupais', 'occupait', 'occupant', 'occupas', 'occupasse', 'occupassent', 'occupasses', 'occupassiez', 'occupassions', 'occupe', 'occupent', 'occuper', 'occupera', 'occuperai', 'occuperaient', 'occuperais', 'occuperait', 'occuperas', 'occuperez', 'occuperiez', 'occuperions', 'occuperons', 'occuperont', 'occupes', 'occupez', 'occupiez', 'occupions', 'occupons', 'occupâmes', 'occupât', 'occupâtes', 'occupèrent', 'occupé', 'occupée', 'occupées', 'occupés', 'occupation', 'occupations', 'cession', 'cessions', 'stocka', 'stockai', 'stockaient', 'stockais', 'stockait', 'stockant', 'stockas', 'stockasse', 'stockassent', 'stockasses', 'stockassiez', 'stockassions', 'stocke', 'stockent', 'stocker', 'stockera', 'stockerai', 'stockeraient', 'stockerais', 'stockerait', 'stockeras', 'stockerez', 'stockeriez', 'stockerions', 'stockerons', 'stockeront', 'stockes', 'stockez', 'stockiez', 'stockions', 'stockons', 'stockâmes', 'stockât', 'stockâtes', 'stockèrent', 'stocké', 'stockée', 'stockées', 'stockés', 'stockage', 'stockages', ]
fneutre = ['débuta', 'débutai', 'débutaient', 'débutais', 'débutait', 'débutant', 'débutas', 'débutasse', 'débutassent', 'débutasses', 'débutassiez', 'débutassions', 'débute', 'débutent', 'débuter', 'débutera', 'débuterai', 'débuteraient', 'débuterais', 'débuterait', 'débuteras', 'débuterez', 'débuteriez', 'débuterions', 'débuterons', 'débuteront', 'débutes', 'débutez', 'débutiez', 'débutions', 'débutons', 'débutâmes', 'débutât', 'débutâtes', 'débutèrent', 'débuté', 'débutée', 'débutées', 'débutés', 'utilisa', 'utilisai', 'utilisaient', 'utilisais', 'utilisait', 'utilisant', 'utilisas', 'utilisasse', 'utilisassent', 'utilisasses', 'utilisassiez', 'utilisassions', 'utilise', 'utilisent', 'utiliser', 'utilisera', 'utiliserai', 'utiliseraient', 'utiliserais', 'utiliserait', 'utiliseras', 'utiliserez', 'utiliseriez', 'utiliserions', 'utiliserons', 'utiliseront', 'utilises', 'utilisez', 'utilisiez', 'utilisions', 'utilisons', 'utilisâmes', 'utilisât', 'utilisâtes', 'utilisèrent', 'utilisé', 'utilisée', 'utilisées', 'utilisés', 'changement', 'changements', 'change', 'changea', 'changeai', 'changeaient', 'changeais', 'changeait', 'changeant', 'changeas', 'changeasse', 'changeassent', 'changeasses', 'changeassiez', 'changeassions', 'changent', 'changeons', 'changer', 'changera', 'changerai', 'changeraient', 'changerais', 'changerait', 'changeras', 'changerez', 'changeriez', 'changerions', 'changerons', 'changeront', 'changes', 'changez', 'changeâmes', 'changeât', 'changeâtes', 'changiez', 'changions', 'changèrent', 'changé', 'changée', 'changées', 'changés', 'modification', 'modifications', 'modifia', 'modifiai', 'modifiaient', 'modifiais', 'modifiait', 'modifiant', 'modifias', 'modifiasse', 'modifiassent', 'modifiasses', 'modifiassiez', 'modifiassions', 'modifie', 'modifient', 'modifier', 'modifiera', 'modifierai', 'modifieraient', 'modifierais', 'modifierait', 'modifieras', 'modifierez', 'modifieriez', 'modifierions', 'modifierons', 'modifieront', 'modifies', 'modifiez', 'modifiiez', 'modifiions', 'modifions', 'modifiâmes', 'modifiât', 'modifiâtes', 'modifièrent', 'modifié', 'modifiée', 'modifiées', 'modifiés', 'met', 'mets', 'mettaient', 'mettais', 'mettait', 'mettant', 'mette', 'mettent', 'mettes', 'mettez', 'mettiez', 'mettions', 'mettons', 'mettra', 'mettrai', 'mettraient', 'mettrais', 'mettrait', 'mettras', 'mettre', 'mettrez', 'mettriez', 'mettrions', 'mettrons', 'mettront', 'mirent', 'mis', 'mise', 'mises', 'misse', 'missent', 'misses', 'missiez', 'missions', 'mit', 'mîmes', 'mît', 'mîtes', 'mis', 'mise', 'mises', 'engage', 'engagea', 'engageai', 'engageaient', 'engageais', 'engageait', 'engageant', 'engageas', 'engageasse', 'engageassent', 'engageasses', 'engageassiez', 'engageassions', 'engagent', 'engageons', 'engager', 'engagera', 'engagerai', 'engageraient', 'engagerais', 'engagerait', 'engageras', 'engagerez', 'engageriez', 'engagerions', 'engagerons', 'engageront', 'engages', 'engagez', 'engageâmes', 'engageât', 'engageâtes', 'engagiez', 'engagions', 'engagèrent', 'engagé', 'engagée', 'engagées', 'engagés', 'engagement', 'engagements', ]


# preparing the training and testing data by extracting the vectors of words from event_sac that corresponding to the sac_de_mots, automatically assign a label to the words in corresponding categories : admin = 5, diag = 4, depol = 3, nuis = 2, indus = 1, neutre = 0

# In[ ]:


X=[]
y=[]
dX=[]
dy=[]
dX5=[]
dy5=[]
dX4=[]
dy4=[]
dX3=[]
dy3=[]
dX2=[]
dy2=[]
dX1=[]
dy1=[]
dX0=[]
dy0=[]
c1=0
c2=0
c3=0
c4=0
c5=0
c6=0
for a,d in event_sac:
    na=a.strip("▁").lower()
    if na in tadmin:
        X.append(d)
        y.append(5)
        c1+=1
    if na in tdiag:
        X.append(d)
        y.append(4)
        c2+=1
    if na in tdepol:
        X.append(d)
        y.append(3)
        c3+=1
    if na in tnuis:
        X.append(d)
        y.append(2)
        c4+=1
    if na in tindus:
        X.append(d)
        y.append(1)
        c5+=1
    if na in tneutre:
        X.append(d)
        y.append(0)
        c6+=1
        
    if na in fadmin:
        dX5.append(d)
        dX.append(d)
        dy5.append(5)
        dy.append(5)
    if na in fdiag:
        dX4.append(d)
        dX.append(d)
        dy4.append(4)
        dy.append(4)
    if na in fdepol:
        dX3.append(d)
        dX.append(d)
        dy3.append(3)
        dy.append(3)
    if na in fnuis:
        dX2.append(d)
        dX.append(d)
        dy2.append(2)
        dy.append(2)
    if na in findus:
        dX1.append(d)
        dX.append(d)
        dy1.append(1)
        dy.append(1)
    if na in fneutre:
        dX0.append(d)
        dX.append(d)
        dy0.append(0)
        dy.append(0)


# load and set machine learning model

# In[ ]:


from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)
#X_test=dX
#y_test=dy
clf = MLPClassifier(solver='adam', alpha=1e-5,hidden_layer_sizes=(100,100,100), random_state=1,max_iter=300,)


# begin training

# In[ ]:


clf.fit(X, y)


# evaluation by categories

# In[ ]:


n5=len(dy5)
n4=len(dy4)
n3=len(dy3)
n2=len(dy2)
n1=len(dy1)
n0=len(dy0)
nall=n5+n4+n3+n2+n1+n0
f5=0
c5=0
f4=0
c4=0
f3=0
c3=0
f2=0
c2=0
f1=0
c1=0
f0=0
c0=0
for i in [0,1,2,3,4,5]:
#for i in [0,1,2,3,4,]:
    
    exec("pre=clf.predict(dX"+str(i)+")")
    exec("ldy=len(dy"+str(i)+")")
    for n in range(ldy):
        c=0
        pred=pre[n]
        exec("gold=dy"+str(i)+"[n]")
        #gold=dy5[n]
        if pred != gold:
            #c+=1
            exec("f"+str(pred)+"+=1")  
        else:
            exec("f"+str(gold)+"+=1")
            exec("c"+str(pred)+"+=1")
            #f5+=1
            #c5+=1

call=c5+c4+c3+c2+c1+c0
fall=f5+f4+f3+f2+f1+f0
#call=c4+c3+c2+c1+c0
#fall=f4+f3+f2+f1+f0


# In[ ]:


#recall in total
rall=call/nall
rall


# In[ ]:


#precision in total
pall=call/fall
pall


# In[ ]:


#f-mesure in total
accall=2*(rall*pall)/(rall+pall)
accall


# registering the evaluation result by categories in a file

# In[ ]:


with open("/media/cdong/Elements/these/Projet/Extractor/eval_JADT/train12_test2.txt", "w", encoding="utf-8") as t:
    for i in [5,4,3,2,1,0]:
        exec("t.write(str(n"+str(i)+")+'\t')")
        exec("print(n"+str(i)+")")
        
        exec("rappel=c"+str(i)+"/n"+str(i))
        print(rappel)
        
        exec("precision=c"+str(i)+"/f"+str(i))
        print(precision)
        
        t.write(str(precision)+"\t"+str(rappel)+"\t")
        
        fmesure=2*(precision*rappel)/(precision+rappel)
        print(fmesure)
        
        t.write(str(fmesure)+"\n")
        print("\n\n")
    t.write(str(nall)+"\t"+str(pall)+"\t"+str(rall)+"\t"+str(accall))


# save model

# In[ ]:


import pickle
with open("/media/cdong/Elements/these/publication/JADT/models/clf_iter2.pickle",'wb') as fw:
    pickle.dump(clf,fw)


# load model

# In[ ]:


with open("/media/cdong/Elements/these/publication/JADT/models/clf_iter2.pickle",'rb') as fr:
    clf=pickle.load(fr)

