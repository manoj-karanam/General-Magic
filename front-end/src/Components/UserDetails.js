import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import styles from '../Css/UserDetails.module.css';

const UserDetails = () => {
  const navigate = useNavigate();
  const [isEditing, setIsEditing] = useState(false);
  const [isEditingExperience, setIsEditingExperience] = useState(null);
  const [isEditingEducation, setIsEditingEducation] = useState(null);
  const [formData, setFormData] = useState({
    firstName: 'John',
    middleName: 'A.',
    lastName: 'Doe',
    pronouns: 'he/him',
    birthday: '1990-01-01',
    phoneNumber: '123-456-7890',
    address: '123 Main St, Anytown, USA'
  });
  const [experiences, setExperiences] = useState([
    {
      title: 'Software Developer',
      employmentType: 'Full-Time',
      companyName: 'ABC Corp',
      location: 'New York, NY',
      locationType: 'On-site',
      startDate: '2019-01-01',
      endDate: '2021-01-01',
      jobDescription: 'Developed various applications...',
      skills: 'JavaScript, React, Node.js'
    }
  ]);
  const [educations, setEducations] = useState([
    {
      schoolName: 'University of ABC',
      degree: 'Bachelor of Science',
      fieldOfStudy: 'Computer Science',
      startDate: '2015-09-01',
      endDate: '2019-05-01',
      grade: '3.8 GPA',
      description: 'Studied computer science and gained valuable skills...',
      skills: 'Java, Python, SQL'
    }
  ]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleExperienceChange = (index, e) => {
    const { name, value } = e.target;
    const updatedExperiences = experiences.map((exp, expIndex) =>
      expIndex === index ? { ...exp, [name]: value } : exp
    );
    setExperiences(updatedExperiences);
  };

  const handleEducationChange = (index, e) => {
    const { name, value } = e.target;
    const updatedEducations = educations.map((edu, eduIndex) =>
      eduIndex === index ? { ...edu, [name]: value } : edu
    );
    setEducations(updatedEducations);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(formData);
    alert('User details submitted!');
    setIsEditing(false);
  };

  const handleExperienceSubmit = (index, e) => {
    e.preventDefault();
    setIsEditingExperience(null);
  };

  const handleEducationSubmit = (index, e) => {
    e.preventDefault();
    setIsEditingEducation(null);
  };

  const handleAddExperience = () => {
    setExperiences([...experiences, {
      title: '',
      employmentType: '',
      companyName: '',
      location: '',
      locationType: '',
      startDate: '',
      endDate: '',
      jobDescription: '',
      skills: ''
    }]);
    setIsEditingExperience(experiences.length);
  };

  const handleAddEducation = () => {
    setEducations([...educations, {
      schoolName: '',
      degree: '',
      fieldOfStudy: '',
      startDate: '',
      endDate: '',
      grade: '',
      description: '',
      skills: ''
    }]);
    setIsEditingEducation(educations.length);
  };

  const handleCancelExperience = (index) => {
    if (experiences[index].title === '') {
      setExperiences(experiences.filter((_, i) => i !== index));
    }
    setIsEditingExperience(null);
  };

  const handleCancelEducation = (index) => {
    if (educations[index].schoolName === '') {
      setEducations(educations.filter((_, i) => i !== index));
    }
    setIsEditingEducation(null);
  };

  const handleDeleteExperience = (index) => {
    setExperiences(experiences.filter((_, i) => i !== index));
  };

  const handleDeleteEducation = (index) => {
    setEducations(educations.filter((_, i) => i !== index));
  };

  return (
    <div>
      <header className="header-nav">
        <h1>General Magic</h1>
      </header>
      <nav className={styles.dashboardNav}>
        <ul>
          <li><Link to="/dashboard">Home</Link></li>
          <li><Link to="/user-details">User Details</Link></li>
          <li><Link to="/logout">Logout</Link></li>
        </ul>
      </nav>
      <div className={styles.userDetailsContainer}>
        <h2>User Details</h2>
        {isEditing ? (
          <form onSubmit={handleSubmit}>
            <div className={styles.formGroup}>
              <label>First Name</label>
              <input
                type="text"
                name="firstName"
                value={formData.firstName}
                onChange={handleChange}
                required
              />
            </div>
            <div className={styles.formGroup}>
              <label>Middle Name</label>
              <input
                type="text"
                name="middleName"
                value={formData.middleName}
                onChange={handleChange}
              />
            </div>
            <div className={styles.formGroup}>
              <label>Last Name</label>
              <input
                type="text"
                name="lastName"
                value={formData.lastName}
                onChange={handleChange}
                required
              />
            </div>
            <div className={styles.formGroup}>
              <label>Pronouns</label>
              <select
                name="pronouns"
                value={formData.pronouns}
                onChange={handleChange}
                required
              >
                <option value="">Select Pronouns</option>
                <option value="she/her">She/Her</option>
                <option value="he/him">He/Him</option>
                <option value="they/them">They/Them</option>
                <option value="other">Other</option>
              </select>
            </div>
            <div className={styles.formGroup}>
              <label>Birthday</label>
              <input
                type="date"
                name="birthday"
                value={formData.birthday}
                onChange={handleChange}
                required
              />
            </div>
            <div className={styles.formGroup}>
              <label>Phone Number</label>
              <input
                type="tel"
                name="phoneNumber"
                value={formData.phoneNumber}
                onChange={handleChange}
                required
              />
            </div>
            <div className={styles.formGroup}>
              <label>Address</label>
              <textarea
                name="address"
                value={formData.address}
                onChange={handleChange}
                required
              ></textarea>
            </div>
            <button type="submit" className={styles.button}>Save Details</button>
            <button type="button" onClick={() => setIsEditing(false)} className={styles.button}>Cancel</button>
          </form>
        ) : (
          <div>
            <p><strong>First Name:</strong> {formData.firstName}</p>
            <p><strong>Middle Name:</strong> {formData.middleName}</p>
            <p><strong>Last Name:</strong> {formData.lastName}</p>
            <p><strong>Pronouns:</strong> {formData.pronouns}</p>
            <p><strong>Birthday:</strong> {formData.birthday}</p>
            <p><strong>Phone Number:</strong> {formData.phoneNumber}</p>
            <p><strong>Address:</strong> {formData.address}</p>
            <button onClick={() => setIsEditing(true)} className={styles.button}>Edit Details</button>
          </div>
        )}
      </div>
      <div className={styles.experienceSection}>
        <h3>Experience</h3>
        {experiences.map((experience, index) => (
          isEditingExperience === index ? (
            <form key={index} onSubmit={(e) => handleExperienceSubmit(index, e)} className={styles.experienceItem}>
              <div className={styles.formGroup}>
                <label>Title</label>
                <input
                  type="text"
                  name="title"
                  value={experience.title}
                  onChange={(e) => handleExperienceChange(index, e)}
                  required
                />
              </div>
              <div className={styles.formGroup}>
                <label>Employment Type</label>
                <select
                  name="employmentType"
                  value={experience.employmentType}
                  onChange={(e) => handleExperienceChange(index, e)}
                  required
                >
                  <option value="">Select Employment Type</option>
                  <option value="Full-Time">Full-Time</option>
                  <option value="Part-Time">Part-Time</option>
                  <option value="Contract">Contract</option>
                  <option value="Internship">Internship</option>
                  <option value="Freelance">Freelance</option>
                </select>
              </div>
              <div className={styles.formGroup}>
                <label>Company Name</label>
                <input
                  type="text"
                  name="companyName"
                  value={experience.companyName}
                  onChange={(e) => handleExperienceChange(index, e)}
                  required
                />
              </div>
              <div className={styles.formGroup}>
                <label>Location</label>
                <input
                  type="text"
                  name="location"
                  value={experience.location}
                  onChange={(e) => handleExperienceChange(index, e)}
                  required
                />
              </div>
              <div className={styles.formGroup}>
                <label>Location Type</label>
                <select
                  name="locationType"
                  value={experience.locationType}
                  onChange={(e) => handleExperienceChange(index, e)}
                  required
                >
                  <option value="">Select Location Type</option>
                  <option value="On-site">On-site</option>
                  <option value="Remote">Remote</option>
                  <option value="Hybrid">Hybrid</option>
                </select>
              </div>
              <div className={styles.formGroup}>
                <label>Start Date</label>
                <input
                  type="date"
                  name="startDate"
                  value={experience.startDate}
                  onChange={(e) => handleExperienceChange(index, e)}
                  required
                />
              </div>
              <div className={styles.formGroup}>
                <label>End Date</label>
                <input
                  type="date"
                  name="endDate"
                  value={experience.endDate}
                  onChange={(e) => handleExperienceChange(index, e)}
                />
              </div>
              <div className={styles.formGroup}>
                <label>Job Description</label>
                <textarea
                  name="jobDescription"
                  value={experience.jobDescription}
                  onChange={(e) => handleExperienceChange(index, e)}
                  required
                ></textarea>
              </div>
              <div className={styles.formGroup}>
                <label>Skills</label>
                <input
                  type="text"
                  name="skills"
                  value={experience.skills}
                  onChange={(e) => handleExperienceChange(index, e)}
                  required
                />
              </div>
              <button type="submit" className={styles.button}>Save Experience</button>
              <button type="button" onClick={() => handleCancelExperience(index)} className={styles.button}>Cancel</button>
            </form>
          ) : (
            <div key={index} className={styles.experienceItem}>
              <p><strong>Title:</strong> {experience.title}</p>
              <p><strong>Employment Type:</strong> {experience.employmentType}</p>
              <p><strong>Company Name:</strong> {experience.companyName}</p>
              <p><strong>Location:</strong> {experience.location}</p>
              <p><strong>Location Type:</strong> {experience.locationType}</p>
              <p><strong>Start Date:</strong> {experience.startDate}</p>
              <p><strong>End Date:</strong> {experience.endDate}</p>
              <p><strong>Job Description:</strong> {experience.jobDescription}</p>
              <p><strong>Skills:</strong> {experience.skills}</p>
              <button onClick={() => setIsEditingExperience(index)} className={styles.button}>Edit Experience</button>
              <button onClick={() => handleDeleteExperience(index)} className={styles.button}>Delete Experience</button>
            </div>
          )
        ))}
        <button onClick={handleAddExperience} className={styles.add_button}>Add Experience</button>
      </div>
      <div className={styles.educationSection}>
        <h3>Education</h3>
        {educations.map((education, index) => (
          isEditingEducation === index ? (
            <form key={index} onSubmit={(e) => handleEducationSubmit(index, e)} className={styles.educationItem}>
              <div className={styles.formGroup}>
                <label>School Name</label>
                <input
                  type="text"
                  name="schoolName"
                  value={education.schoolName}
                  onChange={(e) => handleEducationChange(index, e)}
                  required
                />
              </div>
              <div className={styles.formGroup}>
                <label>Degree</label>
                <input
                  type="text"
                  name="degree"
                  value={education.degree}
                  onChange={(e) => handleEducationChange(index, e)}
                  required
                />
              </div>
              <div className={styles.formGroup}>
                <label>Field of Study</label>
                <input
                  type="text"
                  name="fieldOfStudy"
                  value={education.fieldOfStudy}
                  onChange={(e) => handleEducationChange(index, e)}
                  required
                />
              </div>
              <div className={styles.formGroup}>
                <label>Start Date</label>
                <input
                  type="date"
                  name="startDate"
                  value={education.startDate}
                  onChange={(e) => handleEducationChange(index, e)}
                  required
                />
              </div>
              <div className={styles.formGroup}>
                <label>End Date</label>
                <input
                  type="date"
                  name="endDate"
                  value={education.endDate}
                  onChange={(e) => handleEducationChange(index, e)}
                />
              </div>
              <div className={styles.formGroup}>
                <label>Grade</label>
                <input
                  type="text"
                  name="grade"
                  value={education.grade}
                  onChange={(e) => handleEducationChange(index, e)}
                />
              </div>
              <div className={styles.formGroup}>
                <label>Description</label>
                <textarea
                  name="description"
                  value={education.description}
                  onChange={(e) => handleEducationChange(index, e)}
                  required
                ></textarea>
              </div>
              <div className={styles.formGroup}>
                <label>Skills</label>
                <input
                  type="text"
                  name="skills"
                  value={education.skills}
                  onChange={(e) => handleEducationChange(index, e)}
                  required
                />
              </div>
              <button type="submit" className={styles.button}>Save Education</button>
              <button type="button" onClick={() => handleCancelEducation(index)} className={styles.button}>Cancel</button>
            </form>
          ) : (
            <div key={index} className={styles.educationItem}>
              <p><strong>School Name:</strong> {education.schoolName}</p>
              <p><strong>Degree:</strong> {education.degree}</p>
              <p><strong>Field of Study:</strong> {education.fieldOfStudy}</p>
              <p><strong>Start Date:</strong> {education.startDate}</p>
              <p><strong>End Date:</strong> {education.endDate}</p>
              <p><strong>Grade:</strong> {education.grade}</p>
              <p><strong>Description:</strong> {education.description}</p>
              <p><strong>Skills:</strong> {education.skills}</p>
              <button onClick={() => setIsEditingEducation(index)} className={styles.button}>Edit Education</button>
              <button onClick={() => handleDeleteEducation(index)} className={styles.button}>Delete Education</button>
            </div>
          )
        ))}
        <button onClick={handleAddEducation} className={styles.add_button}>Add Education</button>
      </div>
    </div>
  );
};

export default UserDetails;
