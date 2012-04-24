#!/usr/bin/env python

from json import dumps
import os

from fom.session import Fluid

fdb = Fluid()
fdb.login('telegraph.co.uk', os.environ['FLUDINFO_TELEGRAPH_PASSWORD'])

datasets = [
    {
        'about': [
            'abu qatada',
            'http://www.guardian.co.uk/commentisfree/2012/apr/17/abu-qatada-taking-the-righton-line',
            'http://www.guardian.co.uk/commentisfree/2012/apr/17/abu-qatada-taking-the-righton-line?INTCMP=SRCH',
            'http://www.guardian.co.uk/commentisfree/cartoon/2012/apr/17/abu-qatada-uk-security-cartoon',
            'http://www.guardian.co.uk/commentisfree/cartoon/2012/apr/17/abu-qatada-uk-security-cartoon?INTCMP=SRCH',
            'http://www.guardian.co.uk/commentisfree/cartoon/2012/apr/19/steve-bell-may-abu-qatada',
            'http://www.guardian.co.uk/commentisfree/cartoon/2012/apr/19/steve-bell-may-abu-qatada?INTCMP=SRCH',
            'http://www.guardian.co.uk/law/2012/apr/19/abu-qatada-deadline-appeal-strasbourg',
            'http://www.guardian.co.uk/law/2012/apr/19/abu-qatada-deadline-appeal-strasbourg?INTCMP=SRCH',
            'http://www.guardian.co.uk/law/2012/apr/19/brighton-abu-qatada-strasbourg',
            'http://www.guardian.co.uk/law/2012/apr/19/brighton-abu-qatada-strasbourg?INTCMP=SRCH',
            'http://www.guardian.co.uk/politics/2012/apr/19/theresa-may-sketch-abu-qatada',
            'http://www.guardian.co.uk/politics/2012/apr/19/theresa-may-sketch-abu-qatada?INTCMP=SRCH',
            'http://www.guardian.co.uk/politics/2012/apr/23/lords-reform-cameron-downplays-referendum',
            'http://www.guardian.co.uk/politics/2012/apr/23/lords-reform-cameron-downplays-referendum?INTCMP=SRCH',
            'http://www.guardian.co.uk/world/2009/feb/19/abu-qatada-profile',
            'http://www.guardian.co.uk/world/2009/feb/19/abu-qatada-profile?INTCMP=SRCH',
            'http://www.guardian.co.uk/world/2012/apr/17/abu-qatada-to-be-deported',
            'http://www.guardian.co.uk/world/2012/apr/17/abu-qatada-to-be-deported?INTCMP=SRCH',
            'http://www.guardian.co.uk/world/2012/apr/18/abu-qatada-deportation-human-rights',
            'http://www.guardian.co.uk/world/2012/apr/18/abu-qatada-deportation-human-rights?INTCMP=SRCH',
            'http://www.guardian.co.uk/world/2012/apr/19/abu-qatada-deportation-farce-clarke',
            'http://www.guardian.co.uk/world/2012/apr/19/abu-qatada-deportation-farce-clarke?INTCMP=SRCH',
            'http://www.guardian.co.uk/world/2012/apr/19/abu-qatada-deportation-so-close',
            'http://www.guardian.co.uk/world/2012/apr/19/abu-qatada-deportation-so-close?INTCMP=SRCH',
            'http://www.guardian.co.uk/world/2012/apr/19/abu-qatada-free-within-weeks',
            'http://www.guardian.co.uk/world/2012/apr/19/abu-qatada-free-within-weeks?INTCMP=SRCH',
            'http://www.guardian.co.uk/world/2012/apr/19/theresa-may-x-factor-qatada',
            'http://www.guardian.co.uk/world/2012/apr/19/theresa-may-x-factor-qatada?INTCMP=SRCH',
            'http://www.guardian.co.uk/world/2012/apr/21/abu-qatada-could-stay-uk',
            'http://www.guardian.co.uk/world/2012/apr/21/abu-qatada-could-stay-uk?INTCMP=SRCH',
            'http://www.guardian.co.uk/world/video/2012/apr/17/theresa-may-abu-qatada-video',
            'http://www.guardian.co.uk/world/video/2012/apr/17/theresa-may-abu-qatada-video?INTCMP=SRCH',
            'http://www.guardian.co.uk/world/video/2012/apr/19/theresa-may-abu-qatada-deadline-video',
            'http://www.guardian.co.uk/world/video/2012/apr/19/theresa-may-abu-qatada-deadline-video?INTCMP=SRCH',
            'http://www.guardian.co.uk/world/abu-qatada?INTCMP=SRCH',
            'http://www.guardian.co.uk/search?q=abu+qatada&section=',
            'http://www.guardian.co.uk/search?q=abu+qatada&target=guardian',
        ],
        'data': dumps(
            [
                {
                    'url': 'http://www.telegraph.co.uk/news/politics/9220928/Transcript-David-Cameron-on-Abu-Qatada-deadline-row.html',
                    'title': 'Transcript: David Cameron on Abu Qatada deadline row',
                    'publication-date': '12:28pm April 23'
                },
                {
                    'url': 'http://www.telegraph.co.uk/news/politics/david-cameron/9220748/David-Cameron-Home-Office-did-check-with-European-Court-over-Abu-Qatada-deportation-deadline.html',
                    'title': 'David Cameron: Home Office did check with European Court over Abu Qatada deportation deadline',
                    'publication-date': '11:40am April 23',
                },
                {
                    'url': 'http://www.telegraph.co.uk/news/uknews/terrorism-in-the-uk/9219700/Theresa-May-facing-more-questions-over-Abu-Qatada-farce.html',
                    'title': 'Theresa May facing more questions over Abu Qatada farce',
                    'publication-date': '6:30am April 23',
                },
                {
                    'url': 'http://www.telegraph.co.uk/news/uknews/terrorism-in-the-uk/9215451/Qatada-free-in-days-after-May-got-the-date-wrong.html',
                    'title': 'Abu Qatada free in days after Theresa May got the date wrong',
                    'publication-date': '10:00pm April 19',
                },
            ]
        ),
    },
    {
        'about': [
            'arsenal',
            'http://www.guardian.co.uk/football/2012/apr/22/arsenal-chelsea-arsene-wenger',
            'http://www.guardian.co.uk/football/2012/apr/22/arsenal-chelsea-arsene-wenger?INTCMP=SRCH',
            'http://www.guardian.co.uk/football/2006/aug/14/theseason2006.sport4',
            'http://www.guardian.co.uk/football/2006/aug/14/theseason2006.sport4?INTCMP=SRCH',
            'http://www.guardian.co.uk/football/2007/aug/12/sport.obsmagspecial13',
            'http://www.guardian.co.uk/football/2007/aug/12/sport.obsmagspecial13?INTCMP=SRCH',
            'http://www.guardian.co.uk/football/2008/aug/11/arsenal',
            'http://www.guardian.co.uk/football/2008/aug/11/arsenal?INTCMP=SRCH',
            'http://www.guardian.co.uk/football/2012/apr/23/cesare-prandelli-mario-balotelli-italy',
            'http://www.guardian.co.uk/football/2012/apr/23/cesare-prandelli-mario-balotelli-italy?INTCMP=SRCH',
            'http://www.guardian.co.uk/football/arsenal',
            'http://www.guardian.co.uk/football/arsenal?INTCMP=SRCH',
            'http://www.guardian.co.uk/football/blog/2012/apr/23/five-things-we-learned-premier-league',
            'http://www.guardian.co.uk/football/blog/2012/apr/23/five-things-we-learned-premier-league?INTCMP=SRCH',
            'http://www.guardian.co.uk/football/blog/2012/apr/23/wayne-rooney-striking-duos-football-tactics',
            'http://www.guardian.co.uk/football/blog/2012/apr/23/wayne-rooney-striking-duos-football-tactics?INTCMP=SRCH',
            'http://www.guardian.co.uk/media/2012/apr/23/the-bridge-1m',
            'http://www.guardian.co.uk/media/2012/apr/23/the-bridge-1m?INTCMP=SRCH',
            'http://www.guardian.co.uk/news/2007/aug/06/guardianspecial4.guardianspecial26',
            'http://www.guardian.co.uk/news/2007/aug/06/guardianspecial4.guardianspecial26?INTCMP=SRCH',
            'http://www.guardian.co.uk/search?q=arsenal&section=',
            'http://www.guardian.co.uk/search?q=arsenal&target=guardian',
            'http://www.guardian.co.uk/football/2012/apr/21/arsenal-chelsea-premier-league-mbm',
            'http://www.guardian.co.uk/football/2012/apr/21/arsenal-chelsea-premier-league-mbm?INTCMP=SRCH',
            'http://www.guardian.co.uk/football/2012/apr/22/tottenham-chelsea-arsenal-newcastle',
            'http://www.guardian.co.uk/football/2012/apr/22/tottenham-chelsea-arsenal-newcastle?INTCMP=SRCH',
            'http://www.guardian.co.uk/football/blog/2012/apr/21/robin-van-persie-player-award-arsenal',
            'http://www.guardian.co.uk/football/blog/2012/apr/21/robin-van-persie-player-award-arsenal?INTCMP=SRCH',
            'http://www.guardian.co.uk/football/blog/2012/apr/21/chelsea-arsenal-top-four',
            'http://www.guardian.co.uk/football/blog/2012/apr/21/chelsea-arsenal-top-four?INTCMP=SRCH',
            'http://www.guardian.co.uk/football/2012/apr/21/chelsea-didier-drogba-fit-barcelona',
            'http://www.guardian.co.uk/football/2012/apr/21/chelsea-didier-drogba-fit-barcelona?INTCMP=SRCH',
            'http://www.guardian.co.uk/football/2012/apr/21/arsenal-chelsea-premier-league',
            'http://www.guardian.co.uk/football/2012/apr/21/arsenal-chelsea-premier-league?INTCMP=SRCH',
            'http://www.guardian.co.uk/football/gallery/2012/apr/21/arsenal-chelsea-in-pictures-gallery',
            'http://www.guardian.co.uk/football/gallery/2012/apr/21/arsenal-chelsea-in-pictures-gallery?INTCMP=SRCH',
            'http://www.guardian.co.uk/football/2012/apr/20/arsene-wenger-robin-van-persie-arsenal',
            'http://www.guardian.co.uk/football/2012/apr/20/arsene-wenger-robin-van-persie-arsenal?INTCMP=SRCH',
            'http://www.guardian.co.uk/football/2012/apr/20/squad-sheets-arsenal-chelsea',
            'http://www.guardian.co.uk/football/2012/apr/20/squad-sheets-arsenal-chelsea?INTCMP=SRCH',
            'http://www.guardian.co.uk/football/2012/apr/19/alan-pardew-chelsea-newcastle-champions-league',
            'http://www.guardian.co.uk/football/2012/apr/19/alan-pardew-chelsea-newcastle-champions-league?INTCMP=SRCH',
            'http://www.guardian.co.uk/football/2012/apr/18/mikel-arteta-injury-out-season',
            'http://www.guardian.co.uk/football/2012/apr/18/mikel-arteta-injury-out-season?INTCMP=SRCH',
            'http://www.guardian.co.uk/football/2012/apr/18/wigan-arsenal-robin-van-persie',
            'http://www.guardian.co.uk/football/2012/apr/18/wigan-arsenal-robin-van-persie?INTCMP=SRCH',
            'http://www.guardian.co.uk/football/2012/apr/17/arsenal-jack-wilshere-euro-2012',
            'http://www.guardian.co.uk/football/2012/apr/17/arsenal-jack-wilshere-euro-2012?INTCMP=SRCH',
            'http://www.guardian.co.uk/football/2012/apr/16/arsenal-wigan-premier-league-report',
            'http://www.guardian.co.uk/football/2012/apr/16/arsenal-wigan-premier-league-report?INTCMP=SRCH',
        ],
        'data': dumps(
            [
                {
                    "publication-date": "1:52pm April 20",
                    "title": "Chelsea's 'battered' striker Didier Drogba out of Arsenal game - and could miss Barcelona return leg",
                    "url": "http://www.telegraph.co.uk/sport/football/teams/chelsea/9216622/Chelseas-battered-striker-Didier-Drogba-out-of-Arsenal-game-and-could-miss-Barcelona-return-leg.html"
                },
                {
                    "publication-date": "11:44am April 19",
                    "title": "Arsenal midfielder Mikel Arteta ruled out for rest of the season as Arsene Wenger faces midfield headache",
                    "url": "http://www.telegraph.co.uk/sport/football/teams/arsenal/9213707/Arsenal-midfielder-Mikel-Arteta-ruled-out-for-rest-of-the-season-as-Arsene-Wenger-faces-midfield-headache.html"
                },
                {
                    "publication-date": "9:00am April 17",
                    "title": "Arsenal midfielder Jack Wilshere to miss Euro 2012 finals",
                    "url": "http://www.telegraph.co.uk/sport/football/teams/england/9208160/Arsenal-midfielder-Jack-Wilshere-to-miss-Euro-2012-finals.html"
                },
                {
                    "publication-date": "8:37am April 17",
                    "title": "Arsenal manager Arsene Wenger blasts Wigan's time-wasting after 2-1 Premier League defeat at home",
                    "url": "http://www.telegraph.co.uk/sport/football/teams/arsenal/9208414/Arsenal-manager-Arsene-Wenger-blasts-Wigans-time-wasting-after-2-1-Premier-League-defeat-at-home.html"
                },
                {
                    "publication-date": "9:46pm April 16",
                    "title": "Arsenal v Wigan Athletic: live",
                    "url": "http://www.telegraph.co.uk/sport/football/competitions/premier-league/9200076/Arsenal-v-Wigan-Athletic-live.html"
                },
                {
                    "publication-date": "7:15am April 16",
                    "title": "Arsene Wenger supports Gary Neville's assertion that diving in English football spread from foreign players",
                    "url": "http://www.telegraph.co.uk/sport/football/teams/arsenal/9205823/Arsene-Wenger-supports-Gary-Nevilles-assertion-that-diving-in-English-football-spread-from-foreign-players.html"
                },
                {
                    "publication-date": "4:00pm April 13",
                    "title": "Arsene Wenger: it is time for video technology in football",
                    "url": "http://www.telegraph.co.uk/sport/football/teams/arsenal/9203162/Arsene-Wenger-it-is-time-for-video-technology-in-football.html"
                },
                {
                    "publication-date": "9:09am April 13",
                    "title": "Arsenal midfielder Yossi Benayoun hails Robin van Persie and Chelsea's Fernando Torres as 'best strikers in world'",
                    "url": "http://www.telegraph.co.uk/sport/football/teams/arsenal/9201836/Arsenal-midfielder-Yossi-Benayoun-hails-Robin-van-Persie-and-Chelseas-Fernando-Torres-as-best-strikers-in-world.html"
                }
            ]
        ),
    },
    {
        'about': [
            'simon cowell',
            'http://www.guardian.co.uk/commentisfree/2012/apr/22/simon-cowell-danni-minogue',
            'http://www.guardian.co.uk/commentisfree/2012/apr/22/simon-cowell-danni-minogue?INTCMP=SRCH',
            'http://www.guardian.co.uk/media/2012/apr/11/britains-got-talent-the-voice',
            'http://www.guardian.co.uk/media/2012/apr/11/britains-got-talent-the-voice?INTCMP=SRCH',
            'http://www.guardian.co.uk/media/2012/apr/17/simon-cowell-biography-daily-mail',
            'http://www.guardian.co.uk/media/2012/apr/17/simon-cowell-biography-daily-mail?INTCMP=SRCH',
            'http://www.guardian.co.uk/media/2012/apr/18/simon-cowell-biographer-access',
            'http://www.guardian.co.uk/media/2012/apr/18/simon-cowell-biographer-access?INTCMP=SRCH',
            'http://www.guardian.co.uk/media/2012/apr/21/simon-cowell-no-sympathy',
            'http://www.guardian.co.uk/media/2012/apr/21/simon-cowell-no-sympathy?INTCMP=SRCH',
            'http://www.guardian.co.uk/commentisfree/2012/mar/26/television-talent-shows',
            'http://www.guardian.co.uk/commentisfree/2012/mar/26/television-talent-shows?INTCMP=SRCH',
            'http://www.guardian.co.uk/media/2012/mar/25/simon-cowell-break-in-charge',
            'http://www.guardian.co.uk/media/2012/mar/25/simon-cowell-break-in-charge?INTCMP=SRCH',
            'http://www.guardian.co.uk/media/mediamonkeyblog/2012/apr/11/simon-cowell-voice-of-god-x-factor',
            'http://www.guardian.co.uk/media/mediamonkeyblog/2012/apr/11/simon-cowell-voice-of-god-x-factor?INTCMP=SRCH',
            'http://www.guardian.co.uk/media/shortcuts/2012/mar/28/simon-cowell-crushed-girls-dream',
            'http://www.guardian.co.uk/media/shortcuts/2012/mar/28/simon-cowell-crushed-girls-dream?INTCMP=SRCH',
            'http://www.guardian.co.uk/media/simoncowell',
            'http://www.guardian.co.uk/media/simoncowell?INTCMP=SRCH',
            'http://www.guardian.co.uk/music/2012/apr/01/labrinth-electronic-earth-review-cowell',
            'http://www.guardian.co.uk/music/2012/apr/01/labrinth-electronic-earth-review-cowell?INTCMP=SRCH',
            'http://www.guardian.co.uk/music/2012/apr/11/one-direction-sued-us-band',
            'http://www.guardian.co.uk/music/2012/apr/11/one-direction-sued-us-band?INTCMP=SRCH',
            'http://www.guardian.co.uk/music/2012/apr/12/britney-spears-us-x-factor',
            'http://www.guardian.co.uk/music/2012/apr/12/britney-spears-us-x-factor?INTCMP=SRCH',
            'http://www.guardian.co.uk/music/2012/mar/29/labrinth-electronic-earth-review',
            'http://www.guardian.co.uk/music/2012/mar/29/labrinth-electronic-earth-review?INTCMP=SRCH',
            'http://www.guardian.co.uk/music/musicblog/2012/apr/17/justin-bieber-simon-cowell',
            'http://www.guardian.co.uk/music/musicblog/2012/apr/17/justin-bieber-simon-cowell?INTCMP=SRCH',
            'http://www.guardian.co.uk/search?q=simon+cowell&section=',
            'http://www.guardian.co.uk/search?q=simon+cowell&target=guardian',
            'http://www.guardian.co.uk/uk/2012/mar/26/woman-remanded-simon-cowell-house',
            'http://www.guardian.co.uk/uk/2012/mar/26/woman-remanded-simon-cowell-house?INTCMP=SRCH',
        ],
        'data': dumps(
            [
                {
                    "publication-date": "8:23pm April 20",
                    "title": "Simon Cowell has only one true love - himself ",
                    "url": "http://www.telegraph.co.uk/culture/tvandradio/simon-cowell/9216745/Simon-Cowell-has-only-one-true-love-himself.html"
                },
                {
                    "publication-date": "10:45am April 23",
                    "title": "Britain's Got Talent: the best lines",
                    "url": "http://www.telegraph.co.uk/culture/tvandradio/britains-got-talent/9188943/Britains-Got-Talent-the-best-lines.html"
                },
                {
                    "publication-date": "8:00am March 27",
                    "title": "Simon Cowell 'intruder arrested by armed police'",
                    "url": "http://www.telegraph.co.uk/culture/tvandradio/simon-cowell/9167086/Simon-Cowell-intruder-arrested-by-armed-police.html"
                },
                {
                    "publication-date": "8:27pm March 25",
                    "title": "Simon Cowell victim of 'aggravated burglary'",
                    "url": "http://www.telegraph.co.uk/culture/tvandradio/simon-cowell/9166175/Simon-Cowell-victim-of-aggravated-burglary.html"
                },
                {
                    "publication-date": "7:00am March 20",
                    "title": "Alesha Dixon loving Britain's Got Talent role",
                    "url": "http://www.telegraph.co.uk/culture/tvandradio/britains-got-talent/9153295/Alesha-Dixon-loving-Britains-Got-Talent-role.html"
                },
                {
                    "publication-date": "10:04am March 19",
                    "title": "Ant and Dec 'angry' with Simon Cowell over late arrival for Britain's Got Talent audition",
                    "url": "http://www.telegraph.co.uk/culture/tvandradio/simon-cowell/9152606/Ant-and-Dec-angry-with-Simon-Cowell-over-late-arrival-for-Britains-Got-Talent-audition.html"
                },
                {
                    "publication-date": "April 6",
                    "title": "It's not too late for Simon Cowell's latest victim",
                    "url": "http://blogs.telegraph.co.uk/culture/stevesilverman/100062282/its-not-too-late-for-simon-cowells-latest-victim/"
                }
            ]
        )
    }
]

for dataset in datasets:
    for about in dataset['about']:
        fdb.about[about]['telegraph.co.uk/posts'].put(dataset['data'])
