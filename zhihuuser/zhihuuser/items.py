# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field,Item


class UserItem(scrapy.Item):

    # define the fields for your item here like:
    id = Field()
    name = Field()
    avatar_url = Field()
    headline = Field()
    description = Field()
    url = Field()
    url_token = Field()
    gender = Field()
    cover_url = Field()
    type = Field()
    badge = Field()

    answer_count = Field()
    articles_count = Field()
    commercial_question_count = Field()
    favorite_count = Field()
    favorited_count = Field()
    follower_count = Field()
    following_columns_count = Field()
    following_count = Field()
    pins_count = Field()
    question_count = Field()
    thank_from_count = Field()
    thank_to_count = Field()
    thanked_count = Field()
    vote_from_count = Field()
    vote_to_count = Field()
    voteup_count = Field()
    following_favlists_count = Field()
    following_question_count = Field()
    following_topic_count = Field()
    marked_answers_count = Field()
    mutual_followees_count = Field()
    hosted_live_count = Field()
    participated_live_count = Field()

    locations = Field()
    educations = Field()
    employments = Field()

    # allow_message: true
    # answer_count: 26
    # articles_count: 0
    # avatar_url: "https://pic1.zhimg.com/v2-0430c430c77863af244e464f02df99b5_is.jpg"
    # avatar_url_template: "https://pic1.zhimg.com/v2-0430c430c77863af244e464f02df99b5_{size}.jpg"
    # badge: []
    # employments: []
    # follower_count: 450
    # gender: 0
    # headline: "甜品店老板娘/猫奴/前证券银行狗"
    # id: "c1deca31ad53e3737dd70a7335205a2b"
    # is_advertiser: false
    # is_blocking: false
    # is_followed: false
    # is_following: false
    # is_org: false
    # name: "倪可儿"
    # type: "people"
    # url: "https://www.zhihu.com/people/ni-ke-er-31"
    # url_token: "ni-ke-er-31"
    # user_type: "people"