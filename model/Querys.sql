CREATE TABLE public.buses (
    bus character varying(255),
    fechahora timestamp with time zone,
    lat double precision,
    lng double precision,
    velocidad double precision,
    pasajeros double precision,
    geom public.geometry,
    vendor character varying(255),
    id integer NOT NULL
);

CREATE TABLE public.paraderosrutas (
    gid integer,
    id bigint,
    codts character varying(15),
    codinfra character varying(15),
    simt character varying(6),
    comuna character varying(19),
    eje character varying(33),
    desdecruce character varying(40),
    haciacruce character varying(34),
    nombre_par character varying(57),
    x double precision,
    y double precision,
    n_et character varying(4),
    n_zp character varying(67),
    zphorario character varying(28),
    frepma double precision,
    frepta double precision,
    nservicios double precision,
    servicios character varying(198),
    geom public.geometry(Point,4326),
    servicio text,
    ogc_fid integer,
    name character varying,
    description character varying,
    "timestamp" timestamp with time zone,
    begin timestamp with time zone,
    "end" timestamp with time zone,
    altitudemode character varying,
    tessellate integer,
    extrude integer,
    visibility integer,
    draworder integer,
    icon character varying,
    route_id integer,
    route_name character varying,
    service_na character varying,
    un integer,
    op_noc character varying,
    dist double precision,
    distpago double precision,
    po_mod character varying,
    sentido character varying,
    cod_usuari character varying,
    cod_ts character varying,
    cod_sinser character varying,
    cod_sinrut character varying,
    cod_ususen character varying,
    tipo_serv integer,
    frec_pm double precision,
    frec_pt double precision,
    plazas_pm double precision,
    plazas_pt double precision,
    sel_pm integer,
    sel_pt integer,
    sen1 integer,
    valida integer,
    wkb_geometry public.geometry(Geometry,4326));

    CREATE TABLE public.buses (
    bus character varying(255),
    fechahora timestamp with time zone,
    lat double precision,
    lng double precision,
    velocidad double precision,
    pasajeros double precision,
    geom public.geometry,
    vendor character varying(255),
    id integer NOT NULL
);

CREATE TABLE public.paraderos2 (
    stop_id character varying(6),
    stop_code character varying(6),
    stop_name character varying,
    stop_lat double precision,
    stop_lon double precision,
    stop_url character varying,
    wheelchair_boarding integer,
    geom public.geometry(Point,4326)
);


-- Vista con los datos a procesar
CREATE VIEW busesparaderoF AS
SELECT p.stop_id AS parader,                                                                      
    p.stop_name,                                                                        
    st_distance(p.geom, buses.geom) AS d,             
    buses.bus,                                        
    buses.fechahora,                                  
    buses.lat,                                        
    buses.lng,                                        
    buses.velocidad,                                  
    buses.pasajeros,                                  
    buses.geom,                                       
    buses.vendor,                                     
    buses.id,
    r.servicio,
    r.nombre_par,
    p.geom as parder_geom,
    p.stop_lat as parder_lat,
    p.stop_lon as parder_lon
FROM paraderos2 p,                             
buses,paraderosrutas r
WHERE ((buses.vendor)::text = (r.cod_sinser)::text) AND ((p.stop_id)::text = (r.simt)::text);


-- Consulta para extraer por csv los datos necesarios para procesar una ruta en específico
COPY SELECT b.* from busesparaderoF b, (SELECT fechahora as fh,min(d) as md from busesparaderoF WHERE servicio='E04I'   GROUP BY fechahora) as gr
WHERE b.servicio='E04I' and d=gr.md and b.fechahora=gr.fh ORDER BY fechahora to '' csv header;

