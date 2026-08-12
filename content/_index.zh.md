---
title:
date: 2022-10-24
type: landing

sections:
  - block: hero
    content:
      title: |
        TransportX
      image:
        filename: img3.jpg
      text: |
        <br>

        **TransportX** 聚焦智能交通领域的科研、教学与实践，推动数据驱动的出行与城市交通创新。

  - block: collection
    content:
      title: 最新动态
      subtitle:
      text:
      count: 5
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: post
      archive:
        enable: true
        text: 查看全部新闻
    design:
      view: card
      columns: '1'

  - block: collection
    content:
      title: 最新组会
      subtitle:
      text:
      count: 5
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: event
      archive:
        enable: true
        text: 查看全部活动
    design:
      view: card
      columns: '1'

  - block: markdown
    content:
      title:
      subtitle: ''
      text:
    design:
      columns: '1'
      background:
        image:
          filename: coders.jpg
          filters:
            brightness: 1
          parallax: false
          position: center
          size: cover
          text_color_light: true
      spacing:
        padding: ['20px', '0', '20px', '0']
      css_class: fullscreen

  - block: collection
    content:
      title: 最新论文
      text: ""
      count: 5
      filters:
        folders:
          - publication
        publication_type: ''
      archive:
        enable: true
        text: 查看全部论文
    design:
      view: citation
      columns: '1'

  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./people/" cta_text="了解团队成员 →" %}}
    design:
      columns: '1'
---
