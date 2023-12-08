-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Хост: localhost
-- Время создания: Дек 08 2023 г., 13:01
-- Версия сервера: 5.7.35-38
-- Версия PHP: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `theeye2014_mp`
--

-- --------------------------------------------------------

--
-- Структура таблицы `wb_content`
--

CREATE TABLE IF NOT EXISTS `wb_content` (
  `nmID` int(11) NOT NULL,
  `wbVendorCode` varchar(30) NOT NULL,
  `brand` varchar(60) NOT NULL,
  UNIQUE KEY `unique_combination` (`nmID`,`wbVendorCode`),
  KEY `idx_wb_content_brand` (`brand`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `wb_imgs`
--

CREATE TABLE IF NOT EXISTS `wb_imgs` (
  `wbImgID` int(11) NOT NULL AUTO_INCREMENT,
  `wbID` int(11) NOT NULL,
  `imgURL` varchar(200) NOT NULL,
  PRIMARY KEY (`wbImgID`),
  UNIQUE KEY `wbImgID` (`wbImgID`),
  UNIQUE KEY `unique_combination` (`wbImgID`,`wbID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `wb_parse`
--

CREATE TABLE IF NOT EXISTS `wb_parse` (
  `wbid` int(11) NOT NULL,
  `pricewb` int(11) NOT NULL,
  `salepricewb` int(11) NOT NULL,
  `brand` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `wb_reviews`
--

CREATE TABLE IF NOT EXISTS `wb_reviews` (
  `idreview` varchar(25) NOT NULL,
  `WBnmID` int(11) NOT NULL,
  `text` text NOT NULL,
  `createdDate` date NOT NULL,
  `userName` varchar(50) NOT NULL,
  `productValuation` int(11) NOT NULL,
  UNIQUE KEY `idreview` (`idreview`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
