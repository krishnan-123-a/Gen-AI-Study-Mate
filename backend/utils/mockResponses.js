/**
 * Demo mode mock responses — used when OPENAI_API_KEY is not set or is a placeholder.
 * All responses are realistic and topic-aware.
 */

const isDemoMode = () => {
  const key = process.env.OPENAI_API_KEY || '';
  return !key || key.startsWith('sk-placeholder') || key === 'your_openai_api_key_here';
};

// ─── CHAT ────────────────────────────────────────────────────────────────────

const chatReplies = [
  (msg) => `Great question! "${msg}" is a fascinating topic. In simple terms, it refers to a concept that builds on foundational principles to create meaningful outcomes. Let me break it down step by step:\n\n1. **Core Idea** — At its heart, this concept is about understanding patterns and applying them systematically.\n2. **Why it matters** — It forms the basis for many advanced topics you'll encounter later.\n3. **Key insight** — The best way to learn it is through practice and real-world examples.\n\nWould you like me to go deeper into any of these points? 😊`,
  (msg) => `Excellent! Let me explain "${msg}" clearly:\n\n📚 **Definition**: This is a fundamental concept in its domain that helps us understand how systems work together.\n\n🔑 **Key Points**:\n• It operates on well-defined rules\n• It has real-world applications across many fields\n• Understanding it unlocks deeper topics\n\n💡 **Simple Analogy**: Think of it like building blocks — each piece connects to form something bigger.\n\nAny follow-up questions? I'm here to help! 🤖`,
  (msg) => `That's a thoughtful question about "${msg}"! Here's a clear explanation:\n\n**Overview**: This topic sits at the intersection of theory and practice. It's widely used because of its reliability and versatility.\n\n**How it works**:\n1. Start with the basic premise\n2. Apply the core rules consistently  \n3. Build toward the solution step by step\n\n**Pro tip**: Try working through a small example first — it makes the abstract concrete very quickly.\n\nKeep asking great questions! 🌟`,
];

const getMockChatReply = (message) => {
  const idx = Math.abs(message.length) % chatReplies.length;
  return chatReplies[idx](message);
};

// ─── TOPICS ──────────────────────────────────────────────────────────────────

const getMockTopicExplanation = (topic, level) => ({
  explanation: `${topic} is a core concept that every ${level} learner should understand. It involves a structured set of principles that work together to solve problems efficiently. At the ${level} level, the focus is on building a strong mental model — understanding not just the "what" but the "why" behind how ${topic} works. Mastery of this topic opens doors to more advanced areas and is widely applicable in real-world scenarios.`,
  keyPoints: [
    `${topic} follows well-defined rules that make it predictable and reliable`,
    `It is widely used across many disciplines and industries`,
    `Understanding ${topic} at the ${level} level requires practice and application`,
    `Breaking it into smaller components makes it much easier to grasp`,
    `Real-world examples accelerate learning significantly`,
  ],
  prerequisites: [
    'Basic logical thinking',
    'Foundational concepts in the domain',
    'Problem-solving fundamentals',
  ],
  nextTopics: [
    `Advanced ${topic}`,
    `${topic} in practice`,
    `Related frameworks and tools`,
    `Real-world applications`,
  ],
  realWorldExample: `Imagine you're building a house. ${topic} is like the architectural blueprint — it defines the structure, ensures everything fits together properly, and guides every decision from foundation to rooftop. Without it, even simple constructions can collapse. With it, complex systems become manageable and elegant.`,
});

// ─── QUIZ ─────────────────────────────────────────────────────────────────────

const getMockQuiz = (topic, count, difficulty) => {
  const base = [
    {
      id: 1,
      question: `What is the primary purpose of ${topic}?`,
      options: [
        'A) To complicate simple problems',
        'B) To provide structured solutions to complex problems',
        'C) To replace human thinking entirely',
        'D) To store data only',
      ],
      answer: 'B) To provide structured solutions to complex problems',
      explanation: `${topic} is fundamentally about providing clear, structured approaches that make complex problems more manageable and solvable.`,
    },
    {
      id: 2,
      question: `Which of the following best describes a key characteristic of ${topic}?`,
      options: [
        'A) It is unpredictable',
        'B) It can only be used by experts',
        'C) It follows well-defined, repeatable principles',
        'D) It applies only to theoretical scenarios',
      ],
      answer: 'C) It follows well-defined, repeatable principles',
      explanation: `One of the defining traits of ${topic} is that its principles are consistent, repeatable, and learnable — making it accessible to anyone who studies it.`,
    },
    {
      id: 3,
      question: `In the context of ${topic}, what does "${difficulty}" difficulty typically imply?`,
      options: [
        `A) Only basic definitions are tested`,
        `B) Questions test application and deeper understanding`,
        `C) The topic is impossible to learn`,
        `D) Prior knowledge is not required`,
      ],
      answer: `B) Questions test application and deeper understanding`,
      explanation: `At ${difficulty} difficulty, you're expected to apply concepts, not just recall definitions — showing true comprehension of ${topic}.`,
    },
    {
      id: 4,
      question: `Which real-world scenario best illustrates ${topic}?`,
      options: [
        'A) Writing a grocery list',
        'B) Designing a systematic solution to a recurring problem',
        'C) Randomly guessing outcomes',
        'D) Memorizing unrelated facts',
      ],
      answer: 'B) Designing a systematic solution to a recurring problem',
      explanation: `${topic} shines most when applied to real, recurring problems where a systematic approach saves time and reduces errors.`,
    },
    {
      id: 5,
      question: `What is the best strategy for mastering ${topic}?`,
      options: [
        'A) Read about it once and move on',
        'B) Avoid practicing until fully confident',
        'C) Combine study with hands-on practice and real examples',
        'D) Focus only on memorizing definitions',
      ],
      answer: 'C) Combine study with hands-on practice and real examples',
      explanation: `Research consistently shows that combining conceptual study with practical application is the most effective way to master ${topic} or any skill.`,
    },
    {
      id: 6,
      question: `How does ${topic} relate to problem-solving?`,
      options: [
        'A) It has no relation to problem-solving',
        'B) It provides a framework that guides systematic problem-solving',
        'C) It only applies to mathematical problems',
        'D) It replaces the need for problem-solving',
      ],
      answer: 'B) It provides a framework that guides systematic problem-solving',
      explanation: `${topic} is deeply intertwined with problem-solving — it gives you a structured lens through which complex problems become tractable.`,
    },
    {
      id: 7,
      question: `Which of these is NOT typically a benefit of understanding ${topic}?`,
      options: [
        'A) Improved logical thinking',
        'B) Ability to tackle complex problems systematically',
        'C) Guaranteed instant expertise in all fields',
        'D) Better understanding of related concepts',
      ],
      answer: 'C) Guaranteed instant expertise in all fields',
      explanation: `While ${topic} offers many benefits, instant expertise in all fields is not one of them — mastery requires consistent practice and experience.`,
    },
    {
      id: 8,
      question: `What makes ${topic} relevant in modern applications?`,
      options: [
        'A) It is only relevant in academic settings',
        'B) Its principles scale from simple to highly complex systems',
        'C) It was invented very recently',
        'D) It requires expensive tools to apply',
      ],
      answer: 'B) Its principles scale from simple to highly complex systems',
      explanation: `The scalability of ${topic} is what makes it enduringly relevant — the same core principles that handle simple cases also power sophisticated real-world systems.`,
    },
    {
      id: 9,
      question: `A student is struggling with ${topic}. What is the MOST effective first step?`,
      options: [
        'A) Skip to advanced topics immediately',
        'B) Review the foundational concepts and work simple examples',
        'C) Give up and study something else',
        'D) Memorize all formulas without understanding them',
      ],
      answer: 'B) Review the foundational concepts and work simple examples',
      explanation: `When struggling with any topic, going back to basics and building understanding through simple examples is almost always the most effective strategy.`,
    },
    {
      id: 10,
      question: `Which analogy best explains how ${topic} works?`,
      options: [
        'A) Like a random number generator — unpredictable and chaotic',
        'B) Like a recipe — follow defined steps to consistently achieve a result',
        'C) Like guessing — no rules, just intuition',
        'D) Like a one-time event — cannot be repeated',
      ],
      answer: 'B) Like a recipe — follow defined steps to consistently achieve a result',
      explanation: `A recipe analogy works beautifully for ${topic}: just as following a recipe reliably produces the same dish, applying ${topic}'s principles reliably produces correct solutions.`,
    },
  ];

  return base.slice(0, Math.min(count, base.length));
};

// ─── FLASHCARDS ───────────────────────────────────────────────────────────────

const getMockFlashcards = (topic, count) => {
  const base = [
    { id: 1,  front: `What is ${topic}?`, back: `${topic} is a fundamental concept that involves structured principles and systematic approaches to understand and solve problems in its domain.` },
    { id: 2,  front: `Why is ${topic} important?`, back: `${topic} is important because it provides a reliable framework for tackling complex problems, forms the basis for advanced topics, and has wide real-world applications.` },
    { id: 3,  front: `What are the core principles of ${topic}?`, back: `The core principles include: (1) structured thinking, (2) repeatable processes, (3) systematic application, and (4) building from simple to complex cases.` },
    { id: 4,  front: `How do you apply ${topic} in practice?`, back: `Apply ${topic} by: identifying the problem, selecting the appropriate technique, following the defined steps methodically, and verifying the result.` },
    { id: 5,  front: `What are common mistakes when learning ${topic}?`, back: `Common mistakes: skipping fundamentals, not practicing enough, memorizing without understanding, and not applying concepts to real problems.` },
    { id: 6,  front: `What prerequisites help you learn ${topic}?`, back: `Helpful prerequisites include: logical reasoning, basic domain knowledge, problem-solving mindset, and familiarity with foundational concepts.` },
    { id: 7,  front: `What topics build on ${topic}?`, back: `Advanced topics that build on ${topic} include higher-level abstractions, specialized applications, performance optimization, and integration with other systems.` },
    { id: 8,  front: `Give a real-world example of ${topic}`, back: `A real-world example: just as an architect uses blueprints (a structured plan) to build a house reliably, ${topic} provides the blueprint for solving problems systematically.` },
    { id: 9,  front: `What is the best way to master ${topic}?`, back: `Mastery comes through: consistent daily practice, working on real projects, teaching it to others, reviewing mistakes, and connecting concepts to real-world scenarios.` },
    { id: 10, front: `How does ${topic} relate to critical thinking?`, back: `${topic} strengthens critical thinking by training you to break down complex problems, identify patterns, evaluate solutions, and reason systematically under constraints.` },
    { id: 11, front: `Define the scope of ${topic}`, back: `The scope of ${topic} spans from beginner applications — where basic rules apply — to advanced scenarios requiring deep expertise and creative problem-solving.` },
    { id: 12, front: `What tools or resources help with ${topic}?`, back: `Useful resources: textbooks, online courses, practice problems, community forums, documentation, and working on projects that apply ${topic} concepts directly.` },
    { id: 13, front: `How is ${topic} tested in academic settings?`, back: `Academically, ${topic} is tested through: multiple-choice questions, problem sets, project work, and practical demonstrations of applying its principles correctly.` },
    { id: 14, front: `What distinguishes a beginner from an expert in ${topic}?`, back: `Beginners follow rules mechanically; experts understand the "why" deeply, recognize patterns quickly, adapt to edge cases, and teach others effectively.` },
    { id: 15, front: `Summarise ${topic} in one sentence`, back: `${topic} is a structured, principled approach that transforms complex challenges into manageable, solvable steps — making it an essential tool in any learner's toolkit.` },
    { id: 16, front: `What is a common misconception about ${topic}?`, back: `A common misconception is that ${topic} is only for experts or only theoretical — in reality, it's practical, learnable at any level, and immediately applicable.` },
    { id: 17, front: `How long does it take to learn ${topic}?`, back: `With consistent effort, foundational understanding can come in days to weeks; true mastery develops over months of practice and real-world application.` },
    { id: 18, front: `What career paths benefit from knowing ${topic}?`, back: `Many careers benefit: software engineering, data science, research, education, engineering, management, and any field that values structured thinking and problem-solving.` },
    { id: 19, front: `How do you explain ${topic} to a complete beginner?`, back: `Tell a beginner: "${topic} is like a set of rules for a game — once you learn the rules, you can play confidently, solve challenges, and even create your own strategies."` },
    { id: 20, front: `What is the history or origin of ${topic}?`, back: `${topic} evolved from foundational work by researchers and practitioners who recognised common patterns in problems. Over time, it was formalised into the systematic framework we study today.` },
  ];

  return base.slice(0, Math.min(count, base.length));
};

module.exports = { isDemoMode, getMockChatReply, getMockTopicExplanation, getMockQuiz, getMockFlashcards };
