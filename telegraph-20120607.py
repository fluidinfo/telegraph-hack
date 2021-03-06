#!/usr/bin/env python

from json import dumps
import os

from fom.session import Fluid

fdb = Fluid()
fdb.login('telegraph.co.uk', os.environ['FLUDINFO_TELEGRAPH_PASSWORD'])

datasets = [
    {
        'about': [
            'euro 2012',
            'euro2012',
            '#euro2012',
            'http://www.guardian.co.uk/football/2012/jun/07/euro-2012-england-jermain-defoe',
            'http://www.guardian.co.uk/football/blog/2012/jun/07/euro-2012-live-blog',
            'http://www.guardian.co.uk/football/blog/2012/jun/06/david-pleat-euro-2012-six-watch',
            'http://www.guardian.co.uk/football/poll/2012/jun/06/euro-2012-who-will-win',
            'http://www.guardian.co.uk/football/2012/jun/06/croatia-slaven-bilic-interview-euro-2012',
            'http://www.guardian.co.uk/football/2012/jun/07/laurent-blanc-rio-ferdinand',
            'http://www.guardian.co.uk/football/blog/2012/jun/07/robert-pires-france-england-euro-2012',
            'http://www.guardian.co.uk/football/2012/jun/07/euro-2012-player-ratings',
            'http://www.guardian.co.uk/football/2012/jun/07/euro-2012-england-rio-ferdinand',
            'http://www.huffingtonpost.co.uk/becky-gamester/euro-2012-england-fans-fl_b_1577010.html',
            'http://www.huffingtonpost.co.uk/2012/06/07/euro-2012-poland-unveil-kazimierz-deyna-statue_n_1576744.html',
            'http://www.huffingtonpost.co.uk/2012/06/07/european-championship-2012-bbc-itv-intros_n_1576806.html',
            'http://www.huffingtonpost.co.uk/2012/06/07/jermain-defoe-leaves-engl_n_1576774.html',
            'http://www.huffingtonpost.co.uk/2012/06/07/englands-european-championship-krakow_n_1576685.html',
            'http://www.guardian.co.uk/football/2012/jun/06/sol-campbell-rio-ferdinand-england',
            'http://www.huffingtonpost.co.uk/2012/06/07/david-bernstein-rio-ferdinand-euro-2012_n_1576604.html',
        ],
        'data': dumps(
            [
                {
                    'url': 'http://www.telegraph.co.uk/sport/football/teams/england/9316621/Euro-2012-Rio-Ferdinand-omission-one-of-those-things-as-brother-Anton-refuses-to-join-condemnation.html',
                    'title': 'Rio Ferdinand omission \'one of those things\' as brother Anton refuses to join condemnation',
                    'publicationDate': '12:43pm Jun 7'
                },
                {
                    'url': 'http://www.telegraph.co.uk/sport/football/competitions/european-championships-2012/9316448/Euro-2012-France-coach-Laurent-Blanc-surprised-at-Rio-Ferdinands-omission-from-Roy-Hodgsons-England-squad.html',
                    'title': 'France coach Laurent Blanc \'surprised\' at Rio Ferdinand\'s omission from Roy Hodgson\'s England squad',
                    'publicationDate': '12:21pm Jun 7'
                },
                {
                    'url': 'http://www.telegraph.co.uk/sport/football/competitions/european-championships-2012/9311098/Euro-2012-Roy-Hodgsons-England-coaching-team.html',
                    'title': 'Euro 2012: Meet Roy Hodgson\'s England coaching team',
                    'publicationDate': '11:47am Jun 7'
                },
                {
                    'url': 'http://www.telegraph.co.uk/sport/football/competitions/european-championships-2012/9313263/Euro-2012-interactive-match-schedule.html',
                    'title': 'Euro 2012 interactive match schedule',
                    'publicationDate': '11:22am Jun 6'
                },
                {
                    'url': 'http://www.telegraph.co.uk/sport/football/competitions/european-championships-2012/9316105/Euro-2012-England-striker-Jermain-Defoe-returns-home-after-death-of-his-father.html',
                    'title': 'England striker Jermain Defoe returns home after death of his father',
                    'publicationDate': '10:14am Jun 7'
                },
                {
                    'url': 'http://www.telegraph.co.uk/sport/football/teams/england/9315881/Euro-2012-FA-can-take-back-my-England-caps-if-proven-true-that-Terry-chosen-over-Ferdinand-because-of-race.html',
                    'title': 'FA can take back my England caps if proven true that Terry chosen over Ferdinand because of race',
                    'publicationDate': '8:47am Jun 7'
                },
                {
                    'url': 'http://www.telegraph.co.uk/sport/football/teams/england/9315368/Euro-2012-Patrice-Evra-amazed-Manchester-United-team-mate-Rio-Ferdinand-not-in-the-England-squad.html',
                    'title': 'Patrice Evra amazed Manchester United team-mate Rio Ferdinand not in the England squad',
                    'publicationDate': '6:05am Jun 7'
                },
                {
                    'url': 'http://www.telegraph.co.uk/sport/football/teams/england/9315471/Euro-2012-Were-good-enough-to-reach-the-final-says-upbeat-Wayne-Rooney.html',
                    'title': 'We\'re good enough to reach the final, says upbeat Wayne Rooney',
                    'publicationDate': '11:30pm Jun 6'
                },
            ]
        ),
    },
    {
        'about': [
            'eurozone crisis',
            'http://www.guardian.co.uk/politics/audio/2012/jun/07/politics-podcast-europe-germany-warsi',
            'http://www.guardian.co.uk/business/2012/jun/07/eurozone-crisis-spain-auction-bailout-rescue',
            'http://www.guardian.co.uk/business/2012/jun/07/germany-take-control-eurozone-crisis',
            'http://www.guardian.co.uk/world/blog/2012/jun/07/david-owen-eu-remedy-referendum',
            'http://www.guardian.co.uk/business/2012/jun/07/george-osborne-optimistic-spanish-banking',
            'http://www.guardian.co.uk/commentisfree/cartoon/2012/jun/06/angela-merkel-eurozone-crisis',
            'http://www.guardian.co.uk/commentisfree/2012/jun/06/euro-crisis-spain',
            'http://www.huffingtonpost.co.uk/2012/06/07/david-cameron-british-taxpayers-will-not-rescue-greek-and-spanish-banks_n_1577937.html',
            'http://www.huffingtonpost.co.uk/2012/06/07/george-osborne-britain-requires-safeguards-from-eurozone-banking-union_n_1576671.html',
            'http://www.huffingtonpost.co.uk/2012/06/07/eurozone-crisis-david-cameron-angela-merkel-eurobonds_n_1576537.html',
        ],
        'data': dumps(
            [
                {
                    'url': 'http://www.telegraph.co.uk/finance/debt-crisis-live/9315476/Debt-crisis-live.html',
                    'title': 'Debt crisis: live',
                    'publicationDate': '7:48pm Jun 7'
                },
                {
                    'url': 'http://www.telegraph.co.uk/news/politics/david-cameron/9317418/David-Cameron-We-wont-take-part-in-EU-banking-union-its-not-our-currency.html',
                    'title': 'David Cameron: We won\'t take part in EU banking union - it\'s not our currency',
                    'publicationDate': '5:00pm Jun 7'
                },
                {
                    'url': 'http://www.telegraph.co.uk/finance/financialcrisis/9316764/George-Osborne-hints-at-British-referendum-on-Europe.html',
                    'title': 'George Osborne hints at British referendum on Europe',
                    'publicationDate': '1:35pm Jun 7'
                },
                {
                    'url': 'http://www.telegraph.co.uk/news/worldnews/europe/eu/9314065/The-euros-guilty-men-are-now-steering-Europe-to-catastrophe.html',
                    'title': 'The euro\'s \'guilty men\' are now steering Europe to catastrophe',
                    'publicationDate': '8:34pm Jun 6'
                },
            ]
        ),
    },
    # {
    #     'about': [
    #     ],
    #     'data': dumps(
    #         [
    #             {
    #                 'url': '',
    #                 'title': '',
    #                 'publicationDate': ''
    #             },
    #         ]
    #     ),
    # },
]

for dataset in datasets:
    for about in dataset['about']:
        fdb.about[about]['telegraph.co.uk/posts'].put(dataset['data'])
