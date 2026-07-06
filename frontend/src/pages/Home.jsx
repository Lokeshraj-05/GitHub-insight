import { useState } from "react";
import axios from "axios";

import ProfileCard from "../components/ProfileCard";
import RepoCard from "../components/RepoCard";
import SkillChart from "../components/SkillChart";
import AIAnalysis from "../components/AIAnalysis";

export default function Home() {

    const [username, setUsername] = useState("");
    const [loading, setLoading] = useState(false);
    const [data, setData] = useState(null);

    const analyze = async () => {

        if (!username) return;

        setLoading(true);

        try {

            const response =
                await axios.get(
                    `http://127.0.0.1:8000/analyze/${username}`
                );

            setData(response.data);

        } catch (err) {
            alert("User not found");
        }

        setLoading(false);
    };

    return (
        <div className="container">

            <h1 className="title">
                GitInsight AI
            </h1>

            <div className="searchBox">

                <input
                    placeholder="Enter GitHub Username"
                    value={username}
                    onChange={(e) =>
                        setUsername(e.target.value)
                    }
                />

                <button onClick={analyze}>
                    Analyze
                </button>

            </div>

            {loading && (
                <h2>
                    Analyzing Profile...
                </h2>
            )}

            {data && (
                <>
                    <ProfileCard
                        profile={data.profile}
                        score={data.score}
                        rating={data.rating}
                    />

                    <SkillChart
                        skills={data.skills}
                    />

                    <AIAnalysis
                        analysis={data.rating}
                    />

                    {data.repositories.map(
                        (repo, index) => (
                            <RepoCard
                                key={index}
                                repo={repo}
                            />
                        )
                    )}
                </>
            )}
        </div>
    );
}