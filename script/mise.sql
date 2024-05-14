-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: May 14, 2024 at 11:30 AM
-- Server version: 8.0.36-0ubuntu0.20.04.1
-- PHP Version: 7.4.3-4ubuntu2.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mise`
--
CREATE DATABASE IF NOT EXISTS `mise` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `mise`;

-- --------------------------------------------------------

--
-- Table structure for table `actionschedule`
--

CREATE TABLE `actionschedule` (
  `id` int NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `fqdn` varchar(255) DEFAULT NULL,
  `hours` varchar(255) DEFAULT NULL,
  `action` varchar(255) DEFAULT NULL,
  `lastrun` datetime DEFAULT NULL,
  `nextrun` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `actionschedule`
--

INSERT INTO `actionschedule` (`id`, `name`, `fqdn`, `hours`, `action`, `lastrun`, `nextrun`) VALUES
(14, 'Taimoor Ahmed', '3/ise32.taimoorlab.local', '6', 'populate', '2023-07-12 18:22:16', '2023-07-13 00:22:16'),
(15, 'sample-backup', '', '6', 'backup', NULL, '2023-07-13 22:40:00'),
(16, 'demo schedule', '9/172.17.30.2', '24', 'populate', NULL, '2023-07-31 11:42:00');

-- --------------------------------------------------------

--
-- Table structure for table `ap`
--

CREATE TABLE `ap` (
  `id` int NOT NULL,
  `ap` varchar(255) DEFAULT NULL,
  `apid` varchar(255) DEFAULT NULL,
  `isename` varchar(255) DEFAULT NULL,
  `queue` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT 'no',
  `get_code` varchar(255) DEFAULT NULL,
  `post_code` varchar(255) DEFAULT NULL,
  `put_code` varchar(255) DEFAULT NULL,
  `href` varchar(255) DEFAULT NULL,
  `time` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `authentication`
--

CREATE TABLE `authentication` (
  `id` int NOT NULL,
  `authentication` varchar(255) DEFAULT NULL,
  `authenticationid` varchar(255) DEFAULT NULL,
  `policyset` varchar(255) DEFAULT NULL,
  `isename` varchar(255) DEFAULT NULL,
  `queue` varchar(255) NOT NULL DEFAULT 'no',
  `get_code` varchar(255) DEFAULT NULL,
  `post_code` varchar(255) DEFAULT NULL,
  `put_code` varchar(255) DEFAULT NULL,
  `href` varchar(255) DEFAULT NULL,
  `time` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `authorization`
--

CREATE TABLE `authorization` (
  `id` int NOT NULL,
  `authorization` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `authorizationid` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `policyset` varchar(255) DEFAULT NULL,
  `isename` varchar(255) DEFAULT NULL,
  `queue` varchar(255) NOT NULL DEFAULT 'no',
  `get_code` varchar(255) DEFAULT NULL,
  `post_code` varchar(255) DEFAULT NULL,
  `put_code` varchar(255) DEFAULT NULL,
  `href` varchar(255) DEFAULT NULL,
  `time` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `authz`
--

CREATE TABLE `authz` (
  `id` int NOT NULL,
  `authz` varchar(255) DEFAULT NULL,
  `authzid` varchar(255) DEFAULT NULL,
  `isename` varchar(255) DEFAULT NULL,
  `queue` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT 'no',
  `get_code` varchar(255) DEFAULT NULL,
  `post_code` varchar(255) DEFAULT NULL,
  `put_code` varchar(255) DEFAULT NULL,
  `href` varchar(255) DEFAULT NULL,
  `time` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `coahistory`
--

CREATE TABLE `coahistory` (
  `id` int NOT NULL,
  `mac` varchar(255) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `response` varchar(255) DEFAULT NULL,
  `message` varchar(255) DEFAULT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `compareauthen`
--

CREATE TABLE `compareauthen` (
  `id` int NOT NULL,
  `random` varchar(255) DEFAULT NULL,
  `authentication` varchar(255) DEFAULT NULL,
  `authenid1` varchar(255) DEFAULT NULL,
  `authenid2` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `compareauthen`
--

INSERT INTO `compareauthen` (`id`, `random`, `authentication`, `authenid1`, `authenid2`) VALUES
(40, '1698104200', 'Authentication Rule 1', '246f9545-bbb8-4f6b-96db-9aa8029e63f3', 'cb01935a-77a5-4002-8c43-d38626ca96f0'),
(41, '1698104200', 'Default', '4998a297-8fbb-4ff8-94db-cd9cadc14a4c', '9d411596-ce98-49a5-a819-70c860d6f08b'),
(42, '1698104220', 'Authentication Rule 1', '246f9545-bbb8-4f6b-96db-9aa8029e63f3', 'cb01935a-77a5-4002-8c43-d38626ca96f0'),
(43, '1698104220', 'Default', '4998a297-8fbb-4ff8-94db-cd9cadc14a4c', '9d411596-ce98-49a5-a819-70c860d6f08b'),
(44, '1698104229', 'Authentication Rule 1', '246f9545-bbb8-4f6b-96db-9aa8029e63f3', 'cb01935a-77a5-4002-8c43-d38626ca96f0'),
(45, '1698104229', 'Default', '4998a297-8fbb-4ff8-94db-cd9cadc14a4c', '9d411596-ce98-49a5-a819-70c860d6f08b'),
(46, '1698104427', 'Authentication Rule 1', '246f9545-bbb8-4f6b-96db-9aa8029e63f3', 'cb01935a-77a5-4002-8c43-d38626ca96f0'),
(47, '1698104427', 'Default', '4998a297-8fbb-4ff8-94db-cd9cadc14a4c', '9d411596-ce98-49a5-a819-70c860d6f08b'),
(48, '1698106027', 'Authentication Rule 1', '246f9545-bbb8-4f6b-96db-9aa8029e63f3', 'cb01935a-77a5-4002-8c43-d38626ca96f0'),
(49, '1698106027', 'Default', '4998a297-8fbb-4ff8-94db-cd9cadc14a4c', '9d411596-ce98-49a5-a819-70c860d6f08b'),
(50, '1698106187', 'Authentication Rule 1', '246f9545-bbb8-4f6b-96db-9aa8029e63f3', 'cb01935a-77a5-4002-8c43-d38626ca96f0'),
(51, '1698106187', 'Default', '4998a297-8fbb-4ff8-94db-cd9cadc14a4c', '9d411596-ce98-49a5-a819-70c860d6f08b'),
(52, '1698106393', 'Authentication Rule 1', '246f9545-bbb8-4f6b-96db-9aa8029e63f3', 'cb01935a-77a5-4002-8c43-d38626ca96f0'),
(53, '1698106393', 'Default', '4998a297-8fbb-4ff8-94db-cd9cadc14a4c', '9d411596-ce98-49a5-a819-70c860d6f08b'),
(54, '1698106409', 'Authentication Rule 1', '246f9545-bbb8-4f6b-96db-9aa8029e63f3', 'cb01935a-77a5-4002-8c43-d38626ca96f0'),
(55, '1698106409', 'Default', '4998a297-8fbb-4ff8-94db-cd9cadc14a4c', '9d411596-ce98-49a5-a819-70c860d6f08b');

-- --------------------------------------------------------

--
-- Table structure for table `cond`
--

CREATE TABLE `cond` (
  `id` int NOT NULL,
  `cond` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `condid` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `isename` varchar(255) DEFAULT NULL,
  `queue` varchar(255) NOT NULL DEFAULT 'no',
  `get_code` varchar(255) DEFAULT NULL,
  `post_code` varchar(255) DEFAULT NULL,
  `put_code` varchar(255) DEFAULT NULL,
  `href` varchar(255) DEFAULT NULL,
  `time` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `credentials`
--

CREATE TABLE `credentials` (
  `id` int NOT NULL,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `radkitid` varchar(255) DEFAULT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `credentials`
--

INSERT INTO `credentials` (`id`, `username`, `password`, `radkitid`, `timestamp`) VALUES
(1, 'admin', 'C1sc0123@', 'sampleradkit', '2023-12-09 01:13:33');

-- --------------------------------------------------------

--
-- Table structure for table `dacl`
--

CREATE TABLE `dacl` (
  `id` int NOT NULL,
  `dacl` varchar(255) DEFAULT NULL,
  `daclid` varchar(255) DEFAULT NULL,
  `isename` varchar(255) DEFAULT NULL,
  `queue` varchar(255) NOT NULL DEFAULT 'no',
  `get_code` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `post_code` varchar(255) DEFAULT NULL,
  `put_code` varchar(255) DEFAULT NULL,
  `href` varchar(255) DEFAULT NULL,
  `time` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `deployhistory`
--

CREATE TABLE `deployhistory` (
  `id` int NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `path` varchar(255) DEFAULT NULL,
  `comments` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `time` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `deploymentcode`
--

CREATE TABLE `deploymentcode` (
  `id` int NOT NULL,
  `element` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `action` varchar(255) DEFAULT NULL,
  `code` varchar(255) DEFAULT NULL,
  `output` varchar(255) DEFAULT NULL,
  `srcise` varchar(255) NOT NULL,
  `dstise` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `deployments`
--

CREATE TABLE `deployments` (
  `id` int NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `fqdn` varchar(255) DEFAULT NULL,
  `credentials` varchar(255) DEFAULT NULL,
  `time` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  `fetched` varchar(255) NOT NULL DEFAULT 'No',
  `fetchedon` timestamp(6) NULL DEFAULT NULL,
  `addedby` varchar(255) DEFAULT NULL,
  `dest` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'no',
  `src` varchar(255) NOT NULL DEFAULT 'no',
  `marked` varchar(255) NOT NULL DEFAULT 'no',
  `reachable` varchar(255) DEFAULT 'no'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `deployschedule`
--

CREATE TABLE `deployschedule` (
  `id` int NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  `comments` varchar(255) DEFAULT NULL,
  `now` varchar(255) NOT NULL DEFAULT 'no',
  `run` varchar(255) NOT NULL DEFAULT 'no'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `deployschedule`
--

INSERT INTO `deployschedule` (`id`, `name`, `time`, `comments`, `now`, `run`) VALUES
(18, 'schedul1', '2023-07-09 14:30:00', 'this is scheduled deployment 1', 'no', 'yes'),
(19, 'sche', '2023-08-24 23:44:00', 'comment1', 'no', 'yes'),
(20, 'deploy_schedule1', '2023-12-29 14:37:00', 'sample for demo', 'no', 'yes');

-- --------------------------------------------------------

--
-- Table structure for table `nad`
--

CREATE TABLE `nad` (
  `id` int NOT NULL,
  `nad` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `nadid` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `isename` varchar(255) DEFAULT NULL,
  `queue` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT 'no',
  `get_code` varchar(255) DEFAULT NULL,
  `post_code` varchar(255) DEFAULT NULL,
  `put_code` varchar(255) DEFAULT NULL,
  `href` varchar(255) DEFAULT NULL,
  `time` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `nodes`
--

CREATE TABLE `nodes` (
  `id` int NOT NULL,
  `fqdn` varchar(255) DEFAULT NULL,
  `node` varchar(255) DEFAULT NULL,
  `ipaddress` varchar(255) DEFAULT NULL,
  `roles` varchar(255) DEFAULT NULL,
  `services` varchar(255) DEFAULT NULL,
  `nodestatus` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `patch`
--

CREATE TABLE `patch` (
  `id` int NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `targetfile` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `time` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `policyset`
--

CREATE TABLE `policyset` (
  `id` int NOT NULL,
  `policyset` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `policysetid` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `isename` varchar(255) DEFAULT NULL,
  `queue` varchar(255) DEFAULT 'no',
  `get_code` varchar(255) DEFAULT NULL,
  `post_code` varchar(255) DEFAULT NULL,
  `put_code` varchar(255) DEFAULT NULL,
  `href` varchar(255) DEFAULT NULL,
  `inheritid` varchar(255) DEFAULT NULL,
  `time` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `policysetdeploy`
--

CREATE TABLE `policysetdeploy` (
  `id` int NOT NULL,
  `comments` varchar(255) DEFAULT NULL,
  `selectedpolicyset` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `radius`
--

CREATE TABLE `radius` (
  `id` int NOT NULL,
  `hostname` varchar(255) NOT NULL DEFAULT '',
  `radiuskey` varchar(255) NOT NULL DEFAULT '',
  `active` varchar(6) NOT NULL DEFAULT 'no',
  `time` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `radius`
--

INSERT INTO `radius` (`id`, `hostname`, `radiuskey`, `active`, `time`) VALUES
(1, 'ise-proxy.taimoorlab.local', 'cisco', 'yes', '2023-05-17 09:59:09.000000');

-- --------------------------------------------------------

--
-- Table structure for table `repo`
--

CREATE TABLE `repo` (
  `id` int NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `path` varchar(255) DEFAULT NULL,
  `uname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `time` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `repo`
--

INSERT INTO `repo` (`id`, `name`, `path`, `uname`, `password`, `time`) VALUES
(1, '10.48.30.76', '/', 'cisco', 'cisco', '2023-03-06 01:32:21.000000');

-- --------------------------------------------------------

--
-- Table structure for table `report`
--

CREATE TABLE `report` (
  `id` int NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `fqdn` varchar(255) DEFAULT NULL,
  `action` varchar(255) DEFAULT NULL,
  `time` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `report`
--

INSERT INTO `report` (`id`, `name`, `fqdn`, `action`, `time`) VALUES
(96, 'my schedule2', '10.52.13.89', 'populate', '2023-06-17 00:45:57'),
(97, 'my schedule2', '10.52.13.89', 'populate', '2023-06-17 00:46:23'),
(98, 'my schedule2', '10.52.13.89', 'populate', '2023-06-17 00:47:33'),
(99, 'my schedule2', '10.52.13.89', 'populate', '2023-06-17 00:48:13'),
(100, 'my schedule2', '10.52.13.89', 'populate', '2023-06-17 00:49:27');

-- --------------------------------------------------------

--
-- Table structure for table `scheduler`
--

CREATE TABLE `scheduler` (
  `id` int NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `fqdn` varchar(255) DEFAULT NULL,
  `action` varchar(255) DEFAULT NULL,
  `frequency` int DEFAULT NULL,
  `scheduler` varchar(255) DEFAULT NULL,
  `addedtime` timestamp(6) NULL DEFAULT CURRENT_TIMESTAMP(6),
  `lastrun` timestamp NULL DEFAULT NULL,
  `nextrun` timestamp NULL DEFAULT '1970-06-17 20:51:59'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `scheduler`
--

INSERT INTO `scheduler` (`id`, `name`, `fqdn`, `action`, `frequency`, `scheduler`, `addedtime`, `lastrun`, `nextrun`) VALUES
(27, 'scheduler1', '1/10.52.13.157', 'Populate.sh', 43200, 'no', '2023-06-18 00:32:54.826171', '2023-06-18 00:57:18', '1970-06-17 20:51:59'),
(28, 'sc', '2/10.52.13.89', 'Populate.sh', 43200, 'no', '2023-06-18 00:33:03.122962', '2023-06-18 00:57:43', '1970-06-17 20:51:59'),
(29, 'sc3', '3/ise32.taimoorlab.local', 'Populate.sh', 43200, 'yes', '2023-06-18 00:33:08.729281', '1970-06-17 20:51:59', '1970-06-17 20:51:59');

-- --------------------------------------------------------

--
-- Table structure for table `sgt`
--

CREATE TABLE `sgt` (
  `id` int NOT NULL,
  `sgt` varchar(255) DEFAULT NULL,
  `sgtid` varchar(255) DEFAULT NULL,
  `isename` varchar(255) DEFAULT NULL,
  `queue` varchar(255) NOT NULL DEFAULT 'no',
  `get_code` varchar(255) DEFAULT NULL,
  `post_code` varchar(255) DEFAULT NULL,
  `put_code` varchar(255) DEFAULT NULL,
  `href` varchar(255) DEFAULT NULL,
  `time` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `uploads`
--

CREATE TABLE `uploads` (
  `id` int NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `time` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `folder` varchar(255) DEFAULT NULL,
  `directory` varchar(255) DEFAULT NULL,
  `queue` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT 'no',
  `post_code` varchar(255) DEFAULT NULL,
  `put_code` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int NOT NULL,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `role` varchar(255) NOT NULL DEFAULT 'Admin',
  `time` timestamp(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `first_name`, `last_name`, `username`, `password`, `role`, `time`) VALUES
(8, 'default', '', 'admin', 'C1sc0123@', 'Admin', '2023-06-16 21:54:38.333008'),
(14, 'Taimoor', 'Ahmed', 'taiahmed', 'C1sc0123@', 'Admin', '2023-06-18 16:00:09.090804'),
(26, 'Hyojin', 'Kim', 'hyojin', 'hyojin', 'Admin', '2024-03-13 09:00:39.900310');

-- --------------------------------------------------------

--
-- Table structure for table `webex`
--

CREATE TABLE `webex` (
  `id` int NOT NULL,
  `token` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT '0',
  `botid` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `webex`
--

INSERT INTO `webex` (`id`, `token`, `botid`) VALUES
(1, 'NmM3ZjliOTMtNjkyYi00ZWI1LTliNjItOGNhNWQ3YmJkYzQ2NWM2YWY5MzItMDA3_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f', 'Y2lzY29zcGFyazovL3VzL0FQUExJQ0FUSU9OLzgxYjk2N2MwLTZiNjktNGIzMC1hYmJlLTZkN2VkZTdmNDRhNA');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `actionschedule`
--
ALTER TABLE `actionschedule`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `ap`
--
ALTER TABLE `ap`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `authentication`
--
ALTER TABLE `authentication`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `authorization`
--
ALTER TABLE `authorization`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `authz`
--
ALTER TABLE `authz`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `coahistory`
--
ALTER TABLE `coahistory`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `compareauthen`
--
ALTER TABLE `compareauthen`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cond`
--
ALTER TABLE `cond`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `credentials`
--
ALTER TABLE `credentials`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dacl`
--
ALTER TABLE `dacl`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `deployhistory`
--
ALTER TABLE `deployhistory`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `deploymentcode`
--
ALTER TABLE `deploymentcode`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `deployments`
--
ALTER TABLE `deployments`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `deployschedule`
--
ALTER TABLE `deployschedule`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `nad`
--
ALTER TABLE `nad`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `nodes`
--
ALTER TABLE `nodes`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `patch`
--
ALTER TABLE `patch`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `policyset`
--
ALTER TABLE `policyset`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `policysetdeploy`
--
ALTER TABLE `policysetdeploy`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `radius`
--
ALTER TABLE `radius`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `repo`
--
ALTER TABLE `repo`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `report`
--
ALTER TABLE `report`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `scheduler`
--
ALTER TABLE `scheduler`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sgt`
--
ALTER TABLE `sgt`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `uploads`
--
ALTER TABLE `uploads`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `webex`
--
ALTER TABLE `webex`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `actionschedule`
--
ALTER TABLE `actionschedule`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `ap`
--
ALTER TABLE `ap`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `authentication`
--
ALTER TABLE `authentication`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `authorization`
--
ALTER TABLE `authorization`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `authz`
--
ALTER TABLE `authz`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `coahistory`
--
ALTER TABLE `coahistory`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `compareauthen`
--
ALTER TABLE `compareauthen`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=56;

--
-- AUTO_INCREMENT for table `cond`
--
ALTER TABLE `cond`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `credentials`
--
ALTER TABLE `credentials`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `dacl`
--
ALTER TABLE `dacl`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `deployhistory`
--
ALTER TABLE `deployhistory`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `deploymentcode`
--
ALTER TABLE `deploymentcode`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `deployments`
--
ALTER TABLE `deployments`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `deployschedule`
--
ALTER TABLE `deployschedule`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `nad`
--
ALTER TABLE `nad`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `nodes`
--
ALTER TABLE `nodes`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `patch`
--
ALTER TABLE `patch`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `policyset`
--
ALTER TABLE `policyset`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `policysetdeploy`
--
ALTER TABLE `policysetdeploy`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `radius`
--
ALTER TABLE `radius`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `repo`
--
ALTER TABLE `repo`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `report`
--
ALTER TABLE `report`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101;

--
-- AUTO_INCREMENT for table `scheduler`
--
ALTER TABLE `scheduler`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `sgt`
--
ALTER TABLE `sgt`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `uploads`
--
ALTER TABLE `uploads`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `webex`
--
ALTER TABLE `webex`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
