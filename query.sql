--create a database 
CREATE DATABASE algtst
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.UTF-8'
    LC_CTYPE = 'en_US.UTF-8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

COMMENT ON DATABASE algtst
    IS 'algtst';
    
--create a schema    
CREATE SCHEMA alg_stg
    AUTHORIZATION postgres;    

--create a table 
CREATE TABLE alg_stg."Shopify_stg"
(
    id character varying(100) COLLATE pg_catalog."default",
    shop_domain character varying(100) COLLATE pg_catalog."default",
    application_id character varying(100) COLLATE pg_catalog."default",
    autocomplete_enabled character varying(100) COLLATE pg_catalog."default",
    user_created_at_least_one_qr character varying(100) COLLATE pg_catalog."default",
    nbr_merchandised_queries character varying(100) COLLATE pg_catalog."default",
    nbrs_pinned_items character varying(100) COLLATE pg_catalog."default",
    showing_logo character varying(100) COLLATE pg_catalog."default",
    has_changed_sort_orders character varying(100) COLLATE pg_catalog."default",
    analytics_enabled character varying(100) COLLATE pg_catalog."default",
    use_metafields character varying(100) COLLATE pg_catalog."default",
    nbr_metafields character varying(100) COLLATE pg_catalog."default",
    use_default_colors character varying(100) COLLATE pg_catalog."default",
    show_products character varying(100) COLLATE pg_catalog."default",
    instant_search_enabled character varying(100) COLLATE pg_catalog."default",
    instant_search_enabled_on_collection character varying(100) COLLATE pg_catalog."default",
    only_using_faceting_on_collection character varying(100) COLLATE pg_catalog."default",
    use_merchandising_for_collection character varying(100) COLLATE pg_catalog."default",
    index_prefix character varying(100) COLLATE pg_catalog."default",
    indexing_paused character varying(100) COLLATE pg_catalog."default",
    install_channel character varying(100) COLLATE pg_catalog."default",
    export_date character varying(100) COLLATE pg_catalog."default",
    has_specific_prefix character varying(100) COLLATE pg_catalog."default",
    date_insert character varying(100) COLLATE pg_catalog."default",
    file_name character varying(200) COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE alg_stg."Shopify_stg"
    OWNER to postgres;
