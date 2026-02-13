---
title: "About"
date: 2020-08-16T15:17:23+09:00
draft: false
description: "Software Engineer based in Tokyo."
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

## Profile

<div class="about-intro">

Software Engineer at an IT company in Tokyo.
Working in a cross-service data platform team, developing and operating products using Scrum.

## Career

<div class="timeline">
  <div class="timeline-item">
    <div class="timeline-date">Apr 2016 — Mar 2020</div>
    <div class="timeline-title">Hiroshima University（B.Eng.）</div>
  </div>
  <div class="timeline-item">
    <div class="timeline-date">Apr 2020 — Mar 2022</div>
    <div class="timeline-title">Nara Institute of Science and Technology（M.Eng.）</div>
  </div>
  <div class="timeline-item">
    <div class="timeline-date">Apr 2022 — Present</div>
    <div class="timeline-title">Software Engineer @ IT Company, Tokyo</div>
  </div>
</div>

## Certifications

- CISSP Associate - ISC2 (2024)
- Registered Information Security Specialist (2023)
- Bookkeeping 2nd Grade (2022)
- Applied Information Technology Engineer (2021)
- G Certificate - JDLA (2020)

## Skills

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

## Contact

- [Google Form](https://forms.gle/jVEM3XQQ6jgRwEwv8)
