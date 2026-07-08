"""
Demo Agent Core Concepts - Think-Act-Observe Loop
"""

class SimpleThoughtAgent:
    """Simplest Agent Demo - Implementing Only Think-Act-Observe Loop"""

    def __init__(self, name="DemoAgent"):
        self.name = name
        self.thoughts = []
        self.actions = []
        self.observations = []
        self.goal = ""

    def run(self, goal):
        """Run Agent until goal achieved or max 3 iterations"""
        print(f"🤖 {self.name} Starting execution for goal: {goal}")
        self.goal = goal

        for i in range(3):
            print(f"\n--- Iteration {i+1}/3 ---")

            # Think
            thought = f"Thinking about how to achieve goal: {goal}"
            self.thoughts.append(thought)
            print(f"💭 Thought: {thought}")

            # Act
            action = f"Executing action related to '{goal}'"
            self.actions.append(action)
            print(f"⚡ Action: {action}")

            # Observe
            success = "goal" in goal and "goal" in action
            observation = f"Action execution result: {'Success' if success else 'Trying'}"
            self.observations.append(observation)
            print(f"👀 Observation: {observation}")

            # Check if goal achieved
            if success and i == 2:  # Third iteration and success
                print(f"\n✅ Goal achieved!")
                break
            elif not success and i == 2:  # Third iteration but not success
                print(f"\n⚠️ Reached max iterations, goal not fully achieved")

        print(f"\n📊 Execution completed:")
        print(f"   Thought count: {len(self.thoughts)}")
        print(f"   Action count: {len(self.actions)}")
        print(f"   Observation count: {len(self.observations)}")

        return {
            "thoughts": self.thoughts.copy(),
            "actions": self.actions.copy(),
            "observations": self.observations.copy()
        }

if __name__ == "__main__":
    print("=" * 40)
    print("Agent Core Concepts Demo")
    print("=" * 40)

    agent = SimpleThoughtAgent("Concept Demo Agent")

    # Test different cases
    test_cases = [
        "Explain what is artificial intelligence",
        "Calculate price after 15% tax",
        "Explain quantum mechanics in simple terms",
        "Write a short poem about spring"
    ]

    for case in test_cases:
        print(f"\n🎯 Test case: {case}")
        result = agent.run(case)
        print()

print("\n✨ Demo completed! This demonstrates the core Think-Act-Observe loop of Agent.")