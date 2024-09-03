--
-- PostgreSQL database dump
--

-- Dumped from database version 16.3
-- Dumped by pg_dump version 16.3

-- Started on 2024-09-03 13:30:20

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 215 (class 1259 OID 16599)
-- Name: employees; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.employees (
    "Name" text,
    "Salary" integer,
    "Position" text,
    "Department" text
);


ALTER TABLE public.employees OWNER TO postgres;

--
-- TOC entry 4830 (class 0 OID 16599)
-- Dependencies: 215
-- Data for Name: employees; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.employees ("Name", "Salary", "Position", "Department") FROM stdin;
Alice	25000	Engineer	Development
Bob	18000	Designer	Marketing
Charlie	22000	Engineer	Development
David	17000	Manager	Sales
Eve	21000	Analyst	Finance
Frank	20000	Engineer	Development
Grace	30000	Developer	IT
Hank	19000	Developer	IT
Ivy	16000	Prospector	Exploration
Jack	23000	Engineer	Development
Kara	15000	Analyst	Finance
Leo	31000	Manager	Management
Mona	27000	Designer	Marketing
Nick	18000	Prospector	Exploration
Olivia	24000	Engineer	Development
Paul	26000	Manager	Sales
Quincy	28000	Analyst	Finance
Rita	29000	Developer	IT
Steve	21000	Prospector	Exploration
Tina	20000	Engineer	Development
\.


-- Completed on 2024-09-03 13:30:21

--
-- PostgreSQL database dump complete
--

