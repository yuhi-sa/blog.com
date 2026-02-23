---
title: "About"
date: 2020-08-16T15:17:23+09:00
draft: false
description: "都内IT企業で働くソフトウェアエンジニア"
---

<!--more-->

<style>
.about-intro {
  font-size: var(--text-lg);
  line-height: var(--leading-relaxed);
  margin-bottom: var(--space-8);
}

/* Timeline */
.timeline {
  position: relative;
  padding-left: 2rem;
}
.timeline::before {
  content: "";
  position: absolute;
  left: 0.5rem;
  top: 0.5rem;
  bottom: 0.5rem;
  width: 2px;
  background: var(--border-light);
}
.timeline-item {
  position: relative;
  margin-bottom: var(--space-6);
}
.timeline-item::before {
  content: "";
  position: absolute;
  left: -1.75rem;
  top: 0.45rem;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--accent);
  border: 2px solid var(--bg-primary);
  box-shadow: 0 0 0 2px var(--accent);
}
.timeline-item:last-child::before {
  box-shadow: 0 0 0 2px var(--accent), 0 0 0 5px var(--accent-light);
}
.timeline-date {
  font-size: var(--text-sm);
  color: var(--text-muted);
  font-weight: var(--font-medium);
}
.timeline-title {
  font-size: var(--text-base);
  font-weight: var(--font-semibold);
  color: var(--text-primary);
  margin: var(--space-1) 0;
}
.timeline-desc {
  font-size: var(--text-sm);
  color: var(--text-secondary);
}

/* Skill Badges */
.skill-category {
  margin-bottom: var(--space-6);
}
.skill-label {
  font-size: var(--text-sm);
  font-weight: var(--font-semibold);
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: var(--space-3);
}
.skill-badges {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-2);
}
.skill-badges img {
  border: none !important;
  margin: 0 !important;
  border-radius: var(--radius-sm) !important;
}

/* About subsection labels */
.about-sub {
  font-size: var(--text-sm);
  font-weight: var(--font-semibold);
  color: var(--text-muted);
  margin-top: var(--space-4);
  margin-bottom: var(--space-1);
}
</style>

## プロフィール

<div class="about-intro">

都内IT企業にてソフトウェアエンジニアとして勤務しています。
サービス横断のデータ利活用を促進する部署に所属し、スクラムを活用したプロダクトの開発と運用に従事しています。

## 経歴

<div class="timeline">
  <div class="timeline-item">
    <div class="timeline-date">2022年4月 〜 現在</div>
    <div class="timeline-title">IT企業にてソフトウェアエンジニアとして勤務</div>
  </div>
</div>
<div class="timeline">
  <div class="timeline-item">
    <div class="timeline-date">2020年4月 〜 2022年3月</div>
    <div class="timeline-title">奈良先端科学技術大学院大学 修了（修士・工学）</div>
  </div>
  <div class="timeline-item">
    <div class="timeline-date">2016年4月 〜 2020年3月</div>
    <div class="timeline-title">広島大学 卒業（学士・工学）</div>
  </div>
</div>

## 資格

- CISSP（準会員）（2024年）
- 情報処理安全確保支援士試験（2023年）
- 日商簿記検定2級（2022年）
- 応用情報技術者試験（2021年）
- G検定（2020年）

## 技術スタック

<div class="skill-category">
  <div class="skill-label">Languages</div>
  <div class="skill-badges">
    <img src="https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=fff" alt="TypeScript" />
    <img src="https://img.shields.io/badge/Java-ED8B00?logo=openjdk&logoColor=fff" alt="Java" />
    <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff" alt="Python" />
    <img src="https://img.shields.io/badge/Go-00ADD8?logo=go&logoColor=fff" alt="Go" />
    <img src="https://img.shields.io/badge/Ruby-CC342D?logo=ruby&logoColor=fff" alt="Ruby" />
    <img src="https://img.shields.io/badge/C-A8B9CC?logo=c&logoColor=000" alt="C" />
    <img src="https://img.shields.io/badge/MATLAB-0076A8?logo=mathworks&logoColor=fff" alt="MATLAB" />
  </div>
</div>

<div class="skill-category">
  <div class="skill-label">Frameworks</div>
  <div class="skill-badges">
    <img src="https://img.shields.io/badge/Next.js-000?logo=nextdotjs&logoColor=fff" alt="Next.js" />
    <img src="https://img.shields.io/badge/Spring%20Boot-6DB33F?logo=springboot&logoColor=fff" alt="Spring Boot" />
    <img src="https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=fff" alt="PyTorch" />
    <img src="https://img.shields.io/badge/Ruby%20on%20Rails-D30001?logo=rubyonrails&logoColor=fff" alt="Ruby on Rails" />
  </div>
</div>

<div class="skill-category">
  <div class="skill-label">Infrastructure & Middleware</div>
  <div class="skill-badges">
    <img src="https://img.shields.io/badge/Kubernetes-326CE5?logo=kubernetes&logoColor=fff" alt="Kubernetes" />
    <img src="https://img.shields.io/badge/Apache%20Kafka-231F20?logo=apachekafka&logoColor=fff" alt="Kafka" />
    <img src="https://img.shields.io/badge/Apache%20Pulsar-188FFF?logo=apachepulsar&logoColor=fff" alt="Pulsar" />
    <img src="https://img.shields.io/badge/Apache%20Spark-E25A1C?logo=apachespark&logoColor=fff" alt="Spark" />
    <img src="https://img.shields.io/badge/Apache%20Hadoop-66CCFF?logo=apachehadoop&logoColor=000" alt="Hadoop" />
    <img src="https://img.shields.io/badge/MySQL-4479A1?logo=mysql&logoColor=fff" alt="MySQL" />
    <img src="https://img.shields.io/badge/Cassandra-1287B1?logo=apachecassandra&logoColor=fff" alt="Cassandra" />
    <img src="https://img.shields.io/badge/Redis-DC382D?logo=redis&logoColor=fff" alt="Redis" />
    <img src="https://img.shields.io/badge/Athenz-2D72D9?logo=data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjZmZmIiB2aWV3Qm94PSIwIDAgMzAgMzAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTI1LjUgMTMuN2MtLjYtLjYtMS41LS42LTIuMSAwbC0yLjUgMi41LTQuNS00LjVjLS42LS42LTEuNS0uNi0yLjEgMGwtNS41IDUuNS0yLjUtMi41Yy0uNi0uNi0xLjUtLjYtMi4xIDBsLTUgNSAxLjQgMS40IDMuNi0zLjYgMi41IDIuNSA1LjUtNS41IDQuNSA0LjVjLjYuNiAxLjUuNiAyLjEgMGw1LjUtNS41IDIuNSAyLjVjLjYuNiAxLjUuNiAyLjEgMGw1LTUtMS40LTEuNHoiLz48L3N2Zz4=&logoColor=fff" alt="Athenz" />
  </div>
</div>

<div class="skill-category">
  <div class="skill-label">Monitoring & Operations</div>
  <div class="skill-badges">
    <img src="https://img.shields.io/badge/Prometheus-E6522C?logo=prometheus&logoColor=fff" alt="Prometheus" />
    <img src="https://img.shields.io/badge/Dynatrace-1496FF?logo=dynatrace&logoColor=fff" alt="Dynatrace" />
    <img src="https://img.shields.io/badge/Splunk-000?logo=splunk&logoColor=fff" alt="Splunk" />
  </div>
</div>

<div class="skill-category">
  <div class="skill-label">Tools</div>
  <div class="skill-badges">
    <img src="https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=fff" alt="GitHub" />
    <img src="https://img.shields.io/badge/GitLab-FC6D26?logo=gitlab&logoColor=fff" alt="GitLab" />
    <img src="https://img.shields.io/badge/ROS-22314E?logo=ros&logoColor=fff" alt="ROS" />
  </div>
</div>

## その他

- [いいなって思った言葉]({{< ref "/posts/Quotations.md" >}})

## 連絡先

- [Google Form](https://forms.gle/jVEM3XQQ6jgRwEwv8)
