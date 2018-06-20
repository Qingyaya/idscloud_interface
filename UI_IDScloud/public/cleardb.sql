delete from app_price 
	where appid in (select tb_sps.entity_id from tb_sps,ids_service_company
		where (tb_sps.companyid = ids_service_company.companyid and  ids_service_company.name='testuienter' ) or tb_sps.createuser='testui');
delete from app_document
	where appid in (select tb_sps.entity_id from tb_sps,ids_service_company
		where (tb_sps.companyid = ids_service_company.companyid and  ids_service_company.name='testuienter' ) or tb_sps.createuser='testui');
delete from app_function
	where EntityID in (select tb_sps.entity_id from tb_sps,ids_service_company
		where (tb_sps.companyid = ids_service_company.companyid and  ids_service_company.name='testuienter' ) or tb_sps.createuser='testui');
delete from tb_sps where companyid in (select companyid from ids_service_company where name='testuienter') or createuser='testui';
delete from ids_org_relation where sorg_id in (select sorg_id from sorg where sorg_name='testuiregister' );
delete from sorg where companyid=(SELECT company_id FROM ids_consume_company WHERE name='testuiregister') AND SORG_FULLNAME<>'testuiregister';
delete from ids_order_relation where company_id =(select company_id from ids_consume_company where name='testuiregister');
delete from ids_company_apps where companyid=(select company_id from ids_consume_company where name='testuiregister');
DELETE from `order` where consume_company_id=(SELECT company_id from ids_consume_company where name='testuiregister');
delete from ids_consume_company where name='testuiregister';
delete from ids_service_company_middle where name='testuienter';
delete from ids_service_company where name='testuienter';
delete from tb_user where display_name in ('testui','userapp01','userapp02','userapp03','userapp04');

