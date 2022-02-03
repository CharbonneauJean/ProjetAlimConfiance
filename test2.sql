select count(*) from mots_cles
select * from motcle_inspection

select * from etablissement


SELECT 1 FROM etablissement WHERE etablissement.libelle_etablissement = 'DISTRIBUeazeTION CASINO FRANCE' group by libelle_etablissement

select count(*) from mots_cles
select count(*) from motcle_inspection



select *,
	CASE 
      WHEN ins.synthese_eval = 'Très satisfaisant'  THEN 4
      WHEN ins.synthese_eval = 'Satisfaisant'  THEN 3
      WHEN ins.synthese_eval = 'A améliorer'  THEN 2
      WHEN ins.synthese_eval = 'A corriger de manière urgente'  THEN 1
	END	as num_synthese
from inspection ins
join etablissement eta on ins.idetablissement = eta.idetablissement
join activite act on act.idactivite = ins.idactivite
where idinspection in (
	select idinspection from motcle_inspection where idmotcle in ( select idmotcle from mots_cles where motcle = 'charbonneau')
	)
order by num_synthese
limit 20

select distinct * from activite

select *,
	CASE 
      WHEN ins.synthese_eval = 'Très satisfaisant'  THEN 4
      WHEN ins.synthese_eval = 'Satisfaisant'  THEN 3
      WHEN ins.synthese_eval = 'A améliorer'  THEN 2
      WHEN ins.synthese_eval = 'A corriger de manière urgente'  THEN 1
	END	as num_synthese
from inspection ins
join etablissement eta on ins.idetablissement = eta.idetablissement
join activite act on act.idactivite = ins.idactivite
where idinspection in (
	select idinspection from motcle_inspection where idmotcle in ( select idmotcle from mots_cles where motcle = 'pizza')
	)
order by num_synthese
limit 10

select count(motcle) from mots_cles where idmotcle in (select idmotcle from motcle_inspection where idinspection in (
	select idinspection from inspection where synthese_eval in ('A améliorer', 'A corriger de manière urgente')
))
and (motcle ~* '[a-z]') is true
order by motcle